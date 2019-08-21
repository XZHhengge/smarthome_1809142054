# -*-coding:utf8-*-
import time
import json
import socket
import threading
from datetime import datetime


def udp(data):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 定义成UDP
    # s.settimeout(10)  # socket发送和接收时间等待时间不能超过10秒

    ip_port = ('0.0.0.0', 23333)
    s.sendto(bytes(data.encode('utf-8')), ip_port)
    # ip_port = ('94.191.87.62', 23333)  # ip,端口
    while True:
        # info = {
        #     'name': '',
        #     'info': 'test',
        #     'status': 'safe',
        #     'number': data,
        #     'time': str(datetime.now())
        # }  # json数据,这是我们要暂时定义好要发的数据,不同wifi模块的Number是不一样的,你可以定义编号
        # json_info = json.dumps(info)
        # s.sendto(bytes(json_info.encode('utf-8')), ip_port)
        # try:  # 错误处理
        receive, addr = s.recvfrom(1024)  # 接收数据和server端的ip地址

        receive = str(receive, encoding='utf-8')  # 转码

        if receive[0:9] == 'heartBeat':
            print('心跳包')
            info = "info:heartbeat-name:{}-status:open-number:5-time:"
            s.sendto(bytes(info.encode('utf-8')), ip_port)
            # print(datetime.now())
        else:
            info = "operation:success-time:azxczzxzx-device-number:12311"
            s.sendto(bytes(info.encode('utf-8')), ip_port)
            print('不是心跳包')
            print(threading.current_thread().name,receive)

        #     name = json.loads(receive)['name']  # 获取json数据里面的name的value值
        #     if name == '':  # 判断是否为空,这个是接收返回来的心跳的数据
        #         # print('心跳包', datetime.now())
        #         continue  # 继续循环
        #     else:  # 如果不为空说明不是心跳包,而是接口传参
        #         print('api传参数',  datetime.now())  # 输出到控制台
        #         info['name'] = name.upper()  # 换成大写
        #         json_info = json.dumps(info)
        #         s.sendto(bytes(json_info.encode('utf-8')), ip_port)  # 在发回去,表明已经收到
        #         print(threading.current_thread().name, receive)  # 输出到控制台
        # except Exception as e:  # 出错后在处理
        #     print(threading.current_thread().name, e, '重传')  # 输出到控制台
        #     continue  # 继续循环
        # time.sleep(1)

if __name__ == '__main__':
    number = ['xxxx', 'yyyy', 'zzzz', 'bbbb']
    for i in number:
        t = threading.Thread(target=udp, args=(i,))
        t.start()