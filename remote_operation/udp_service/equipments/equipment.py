#coding:utf-8

import setting
import time
import random



class Equipment(object):
    '''所有设备类型的基类
    ip_address       设备IP地址\n
    mac_address      设备MAC地址\n
    first_type       一级类型\n
    second_type      二级类型\n
    equipment_number 设备编号\n
    status           设备状态\n
    '''
    def __init__(self, ip_address, mac_address, first_type, second_type, status):
        self.ip_address = ip_address
        self.mac_address = mac_address
        self.first_type = first_type
        self.second_type = second_type

        self.status = status

        self.heartbeat = setting.HB_INITCOUNT


    # def updata(self, first_type=None, second_type=None, equipment_number=None, status=None):
    #     '''更新设备数据'''
    #     if first_type: self.first_type = first_type
    #     if second_type: self.second_type = second_type
    #     if equipment_number: self.equipment_number = equipment_number
    #     if status: self.status = status

    def get_first_type(self):
        '''获取一级类型'''
        return self.first_type

    def get_second_type(self):
        '''获取二级类型'''
        return self.second_type

    def get_status(self):
        '''获取设备状态'''
        return self.status

    def set_status(self, status):
        '''设置设备状态'''
        self.status =status

    def get_heartbeat(self):
        '''获取心跳包计数'''
        return self.heartbeat

    def reset_heartbeat(self):
        '''重置心跳包计数'''
        self.heartbeat = setting.HB_INITCOUNT

    def reduce_heartbeat(self):
        '''减少心跳包计次'''
        self.heartbeat -= setting.HB_REDUCTION

