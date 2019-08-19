#coding:utf-8

from device import Device

class AirConditioner(Device):
    '''空调类'''


    def __init__(self, ip_address, first_type, second_type, device_number, status, mac_address='FF:FF:FF:FF:FF:FF',):
        super(AirConditioner, self).__init__(ip_address, mac_address, first_type, second_type, device_number, status)
    pass
