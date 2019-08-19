#coding:utf-8

# from remote_operation.models import autologging
import json
import os, django
# from django.core.wsgi import get_wsgi_application
# sys.path.append(os.path.dirname(os.path.abspath('.')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smarthome_1809142054.settings')
# application = get_wsgi_application()
django.setup()
# from udp_service.equipments.equipment_manager import EquipmentManager
# from equipment.equipment import Equipment
# from udp_service.equipments.light import Light
# from udp_service.equipments.ceiling_fan import CeilingFan
# from udp_service.equipments.air_conditioner import AirConditioner

import threading
import socket
from .import setting

from remote_operation.models import Device

global equipment_manager
global udp_socket
# global ip_address
# udp_socket = socket(AF_INET, SOCK_DGRAM)
global ip_address

def heartbeat_handler():
    '''定时递减心跳包计数'''
    global equipment_manager
    # LOG START
    ##log = autoautologging(level="INFO", message="heartbeat_handler start completion")
    #log.save()
    # LOG END

    # 循环监听
    startTime = time.time()
    while True:
        # 减少心跳包计数
        if time.time() - startTime >= setting.HB_REDUCTION:
            equipment_manager.reduce_heartbeat()
            startTime = time.time()

# def create_equipment_object(ip_address, current_status, equipment_info):
#     '''创建设备对象'''
#
#     # 驱动器设备
#     if 'device_number' in equipment_info:
#         if equipment_info['first_type'] == 'AABC': # 被控设备
#             if equipment_info['second_type'] == 'AADG': # 灯管
#                 new_equipment = Light(ip_address=ip_address,
#                                       first_type=equipment_info['first_type'],
#                                       second_type=equipment_info['second_type'],
#                                       device_number=equipment_info['device_number'],
#                                       status=current_status)
#                 return new_equipment
#
#             if equipment_info['second_type'] == 'AACL': # 窗帘
#                 new_equipment = Light(ip_address=ip_address,
#                                       first_type=equipment_info['first_type'],
#                                       second_type=equipment_info['second_type'],
#                                       device_number=equipment_info['device_number'],
#                                       status=current_status)
#                 return new_equipment
#
#             if equipment_info['second_type'] == 'AAFS': # 风扇
#                 new_equipment = CeilingFan(ip_address=ip_address,
#                                            first_type=equipment_info['first_type'],
#                                            second_type=equipment_info['second_type'],
#                                            device_number=equipment_info['device_number'],
#                                            status=current_status)
#                 return new_equipment
#
#             if equipment_info['second_type'] == 'AAKT': # 空调
#                 new_equipment = AirConditioner(ip_address=ip_address,
#                                                first_type=equipment_info['first_type'],
#                                                second_type=equipment_info['second_type'],
#                                                device_number=equipment_info['device_number'],
#                                                status=current_status)
#                 return new_equipment
#
#     # 控制器设备
#     if 'product_number' in equipment_info:
#         if equipment_info['first_type'] == 'AAKG': # 开关
#             if equipment_info['second_type'] == 'AACL': # 窗帘
#                 new_equipment = Light(ip_address=ip_address,
#                                       first_type=equipment_info['first_type'],
#                                       second_type=equipment_info['second_type'],
#                                       device_number=equipment_info['product_number'],
#                                       status=current_status)
#                 return new_equipment
#
#     return None

# def control_light(number, operation):
#     '''电灯控制'''
#     light_status = [
#         [["2","02_00_01"], ["2","02_00_00"]],
#         [["2","01_00_02"], ["2","00_00_02"]],
#         [["1","01_00_02"], ["1","00_00_02"]],
#         [["1","02_00_01"], ["1","02_00_00"]]
#     ]
#
#     if operation == "on":
#         device_number, command = light_status[int(number)-1][0]
#     elif operation == "off":
#         device_number, command = light_status[int(number)-1][1]
#     else:
#         return False
#     print(device_number, command)
#     equipment_info = {'first_type': "AABC",'second_type': "AADG",'device_number': device_number}
#     response_equipment = equipment_manager.find_equipment(equipment_info)
#     if response_equipment:
#         for i in range(setting.ORDER_TIMEOUT):
#             udp_socket.sendto("#{}${}@".format(command, 'FFFFFFFF'), response_equipment.ip_address)
#             time.sleep(1)
#             final_state = response_equipment.get_status()
#             if final_state == command:
#                 return True
#         return False
#     else:
#         print('Equipment does not exist.')
#         return False

# def control_fan(number, operation):
#     '''电扇控制'''
#
#     if operation == "0":
#         command = CeilingFan.STOP_GEAR
#     elif operation == "1":
#         command = CeilingFan.FIRST_GEAR
#     elif operation == "2":
#         command = CeilingFan.SECOND_GEAR
#     elif operation == "3":
#         command = CeilingFan.THIRD_GEAR
#     else:
#         print("Command error : {}".format(operation))
#         return False
#
#     equipment_info = {'first_type': "AABC",'second_type': "AAFS",'device_number': number}
#     response_equipment = equipment_manager.find_equipment(equipment_info)
#     if response_equipment:
#         for i in range(setting.ORDER_TIMEOUT):
#             udp_socket.sendto("#{}${}@".format(command, 'FFFFFFFF'), response_equipment.ip_address)
#             time.sleep(1)
#             final_state = response_equipment.get_status()
#             if final_state == command:
#                 return True
#         return False
#     else:
#         print('Equipment does not exist.')
#         return False


# def control_curtain(number, operation):
#     '''窗帘控制'''
#
#     if operation == "open":
#         command = "01_10_01"
#     elif operation == "stop":
#         command = "00_00_00"
#     elif operation == "close":
#         command = "00_10_01"
#     else:
#         print("Command error : {}".format(operation))
#         return False
#
#     if number == "1":
#         equipment_info = {'first_type': "AABC",'second_type': "AACL",'device_number': "3"}
#     elif number == "2":
#         equipment_info = {'first_type': "AABC",'second_type': "AACL",'device_number': "2"}
#     elif number == "3":
#         equipment_info = {'first_type': "AABC",'second_type': "AACL",'device_number': "1"}
#     else:
#         print("Command error : {}".format(operation))
#         return False
#
#     response_equipment = equipment_manager.find_equipment(equipment_info)
#     if response_equipment:
#         for i in range(setting.ORDER_TIMEOUT):
#             udp_socket.sendto("#{}${}@".format(command, 'FFFFFFFF'), response_equipment.ip_address)
#             time.sleep(1)
#             final_state = response_equipment.get_status()
#             if final_state == command:
#                 return True
#         return False
#     else:
#         print('Equipment does not exist.')
#         return False

# def control_air_conditioner(number, model, operation):
#     '''空调'''
#     cmd_model = "air_type_033!"
#
#     cmd = ""
#
#     if operation == "on":
#         cmd = "air_power_on!"
#     elif operation == "off":
#         cmd = "air_power_off!"
#     elif operation != None and int(operation) >= 17 and int(operation) <= 30:
#         temp = int(operation)
#         cmd = "air_temp_{}!".format(temp)
#     else:
#         print("Command error : {}".format(operation))
#         return False
#
#     if number == "1":
#         equipment_info = {'first_type': "AABC",'second_type': "AAKT",'device_number': "ACCF23DA96BB"}
#     else:
#         print("Command error : {}".format(operation))
#         return False
#
#     response_equipment = equipment_manager.find_equipment(equipment_info)
#     if response_equipment:
#         for i in range(setting.ORDER_TIMEOUT):
#             if response_equipment.get_status() != cmd_model:
#                 udp_socket.sendto("#{}${}@".format(cmd_model, 'FFFFFFFF'), response_equipment.ip_address)
#                 time.sleep(1)
#             udp_socket.sendto("#{}${}@".format(cmd, 'FFFFFFFF'), response_equipment.ip_address)
#             time.sleep(1)
#             final_state = response_equipment.get_status()
#             if final_state == cmd:
#                 return True
#         return False
#     else:
#         print('Equipment does not exist.')
#         return False


# def get_online_equipment():
#     '''获取所有当前在线的设备的信息
#     信息包括设备识别码和状态,例如:
#     [
#         {'code': AAAA-BBBB-3, 'status': 00_00_00},
#         {'code': AAAA-BBBB-4, 'status': 01_00_00},
#         {'code': AAAA-BBBB-5, 'status': 00_00_01}
#     ]
#     '''
#     return equipment_manager.get_equipment_all()

# def get_registered_equipment():
#     '''获取已注册的设备'''
#     return equipment_manager.get_equipment_all()

# def get_equipment_status(first_type, second_type, device_number):
#     '''获取一台在线设备的状态
#     例如: '00_00_00'
#     '''
#     equipment_info = {'first_type': first_type,'second_type': second_type,'device_number': device_number}
#     equipment = equipment_manager.find_equipment(equipment_info)
#     if equipment:
#         return equipment.get_status()
#     else:
#         return None

import time
#{"first_type":"AABC","second_type":"AAFS","device_number":"2","operation":"00_00_01"}
def udp_handler():

    try:
        global udp_socket
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.bind(('0.0.0.0', 23333))
        # udp_socket.settimeout(5)
        print("waiting to receive messages...")
        while True:

            udp_data, ip_address = udp_socket.recvfrom(1024)
            if udp_data in [b'XXXX', b'ZZZZ', b'YYYY', b'BBBB']:
                print(udp_data)
            else:
                str_data = str(udp_data, encoding='utf-8')
                number = json.loads(str_data)['number']
                print(udp_data)
                if Device.objects.filter(number=number):
                    device = Device.objects.get(number=number)
                    device.ip_port = ip_address
                    device.save()
                else:
                    print(ip_address)
                    Device.objects.create(number=number, ip_port=ip_address).save()
                while True:
                    udp_socket.sendto(udp_data.upper(), ip_address)
                    time.sleep(0.5)
                    if(udp_socket.recvfrom(1024)):
                        print('有返回值')
                        break
                    else:
                        print('重传')
                        continue
                # print('udp_socket.getpeername()', udp_socket.getpeername())
                print(ip_address)
                print(udp_data)
                # print(datetime.now())
                time.sleep(1)
    except Exception as e:
        print(e)


def send(data, ip_port):
    print('send')
    flag = float
    n = 0
    global udp_socket
    while True:
        udp_socket.sendto(bytes(data, encoding='utf-8'), eval(ip_port))
        # time.sleep(0.5)
        dat, ip_port = udp_socket.recvfrom(1024)
        print(dat)
        if dat in [b'XXXX', b'YYYY', b'ZZZZ', b'BBBB']:
            # print()
            print('send有返回值')
            flag = True
            break
        elif dat not in ['XXXX', 'YYYY', 'ZZZZ', 'BBBB']:
            pass
        else:
            n+=1
            print('重传第{}次'.format(n))
            if n == 5:
                flag = False
                break
            else:
                continue
    return flag




# def tcp():
#     s = socket(AF_INET, SOCK_STREAM)
#     s.bind(('0.0.0.0', 9997))
#     s.listen(5)
#     while True:
#         sock, ip_address = s.accept()
#         udp_data = sock.recv(1024)
#         print(udp_data)
#         if Device.objects.filter(number=str(udp_data, encoding='utf-8')):
#             device = Device.objects.get(number=str(udp_data, encoding='utf-8'))
#             device.ip_port = ip_address
#             device.save()
#         else:
#             print(ip_address)
#             Device.objects.create(number=str(udp_data, encoding='utf-8'), ip_port=ip_address).save()
#         sock.send(udp_data.upper())

        
def main():
    # 创建智能设备管理器
    # global equipment_manager
    # equipment_manager = EquipmentManager()

    # 启动心跳包计数线程
    # heartbeat_thread = threading.Thread(target=heartbeat_handler)
    # heartbeat_thread.setDaemon(True)
    # heartbeat_thread.start()

    # 启动UDP处理线程
    udp_thread = threading.Thread(target=udp_handler)
    udp_thread.setDaemon(True)
    udp_thread.start()
    print('开启UDP处理线程')


    while True:
        pass
if __name__ == '__main__':
    main()









