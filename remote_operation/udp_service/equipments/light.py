#coding:utf-8

from device import Device

class Light(Device):
    '''电灯类'''

    LIGHT1_ON  = '01_00_01' # 电灯01开
    LIGHT1_OFF = '01_00_00' # 电灯01关
    LIGHT2_ON  = '02_00_01' # 电灯02开
    LIGHT2_OFF = '02_00_00' # 电灯02关
    LIGHT_ALL_OFF = '00_00_00'
    LIGHT_ALL_ON = ''
    LIGHT1_ON_LIGHT2_OFF = ''
    LIGHT1_OFF_LIGHT_2ON = ''

    def __init__(self, ip_address, first_type, second_type, device_number, status, mac_address='FF:FF:FF:FF:FF:FF',):
        super(Light, self).__init__(ip_address, mac_address, first_type, second_type, device_number, status)

    def get_order_turn_on_light_1(self):
        '''获取打开一号灯的指令'''
        order = "#{}${}@".format(Light.LIGHT1_ON, self._get_order_check_number())
        return order

    def get_order_turn_off_light_1(self):
        '''获取关闭一号灯的指令'''
        order = "#{}${}@".format(Light.LIGHT1_OFF, self._get_order_check_number())
        return order

    def get_order_turn_on_light_2(self):
        '''获取打开二号灯的指令'''
        order = "#{}${}@".format(Light.LIGHT2_ON, self._get_order_check_number())
        return order

    def get_order_turn_off_light_2(self):
        '''获取关闭二号灯的指令'''
        order = "#{}${}@".format(Light.LIGHT2_OFF, self._get_order_check_number())
        return order
    