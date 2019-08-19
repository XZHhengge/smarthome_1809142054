#coding:utf-8

from device import Device

class CeilingFan(Device):
    '''吊扇类'''



    STOP_GEAR   = '00_00_00' # 吊扇关闭
    FIRST_GEAR  = '00_00_01' # 吊扇一档
    SECOND_GEAR = '00_00_10' # 吊扇二档
    THIRD_GEAR  = '00_00_11' # 吊扇三档

    def __init__(self, ip_address, first_type, second_type, device_number, status, mac_address='FF:FF:FF:FF:FF:FF',):
        super(CeilingFan, self).__init__(ip_address, mac_address, first_type, second_type, device_number, status)

    def get_order_stop_gear(self):
        '''获取关闭吊扇的指令'''
        
        order = "#{}${}@".format(CeilingFan.STOP_GEAR, self._get_order_check_number())
        return order

    def get_order_first_gear(self):
        '''获取切换到第一档的指令'''
        order = "#{}${}@".format(CeilingFan.FIRST_GEAR, self._get_order_check_number())
        return order

    def get_order_second_gear(self):
        '''获取切换到第二档的指令'''
        order = "#{}${}@".format(CeilingFan.SECOND_GEAR, self._get_order_check_number())
        return order

    def get_order_third_gear(self):
        '''获取切换到第三档的指令'''
        order = "#{}${}@".format(CeilingFan.THIRD_GEAR, self._get_order_check_number())
        return order
    
