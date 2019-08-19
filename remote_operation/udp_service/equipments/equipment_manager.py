#coding:utf-8

# from remote_operation.models import autologging

# 将顶级目录加入sys.path以导入上级模块(加入第一搜索优先级防止其他文件内有同名模块导致导入失败)
import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)


import setting

class EquipmentManager:
    '''设备管理器,自动化管理在线的设备'''


    def __init__(self):
        self.equipment_group = [] # 设备组


    def reduce_heartbeat(self):
        '''递减心跳包计次,自动移除无响应设备'''
        for equipment in self.equipment_group:
            if equipment.get_heartbeat() <= setting.HB_REDUCTION:
                # LOG START
                #log = autologging(level="INFO", message="equipment has died: {} {}-{}-{}".format(equipment.ip_address,
                                                                                            #  equipment.get_first_type(),
                                                                                            #  equipment.get_second_type(),
                                                                                            #  equipment.get_equipment_number()))
                #log.save()
                # LOG END
                self.equipment_group.remove(equipment)
            else:
                equipment.reduce_heartbeat()
    
    def register_equipment(self, new_equipment):
        '''注册新设备,成功返回True,若设备已存在则返回False'''
        equipment_info = new_equipment.get_equipment_info()
        for equipment in self.equipment_group:
            if equipment.get_equipment_info() == equipment_info:
                return False
        self.equipment_group.append(new_equipment)
        return True

    def find_equipment(self, equipment_info):
        '''查找已注册的设备'''
        
        for equipment in self.equipment_group:
            if equipment.get_equipment_info() == equipment_info:
                return equipment
        return None

    def get_equipment_all(self):
        '''返回当前设备列表'''
        '''注意此功能未正式开放'''
        # return copy.deepcopy(self.equipment_group)
        equipments = []
        for equipment in self.equipment_group:
            equipment_info = {}
            equipment_info['code'] = '{}:{} {}-{}-{}'.format(equipment.ip_address[0], equipment.ip_address[1], equipment.get_first_type(), equipment.get_second_type(), equipment.get_equipment_number())
            equipment_info['status'] = equipment.get_status()
            equipments.append(equipment_info)
        return equipments