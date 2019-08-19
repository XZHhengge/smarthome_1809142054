#coding:utf-8


from equipment import Equipment
import time
import random
class Device(Equipment):
    '''驱动器类
    例如电灯、风扇、窗帘都属于驱动器类，驱动器是他们的父类
    '''
    
    def __init__(self, ip_address, mac_address, first_type, second_type, device_number, status):
        super(Device, self).__init__(ip_address, mac_address, first_type, second_type, status)
        self.device_number = device_number
        self._count = 0 # 计次位
        self._ocn = '' # 指令效验码
        self._lock = False # 指令发送锁

    def get_equipment_number(self):
        '''获取设备编号'''
        return self.device_number

    def get_equipment_info(self):
        '''获取驱动器信息'''
        return {'first_type': self.first_type, 'second_type': self.second_type, 'device_number': self.device_number}

    def _get_order_check_number(self):

        '''获取指令校验码
        指令效验码即Order Check Number,缩写OCN，用于唯一标识一条指令.
        由"五位毫秒级时间戳的后六位的十六进制表示"加上"两位随机数"和"一位计次数"组成
        '''

        self._lock = True # 加上指令锁,在确认指令送达成功前都不允许发送其他指令

        self._count += 1
        if self._count >= 10: self._count = 0

        timestamp = hex((int(round(time.time() * 1000)))%1000000)[2:-1].zfill(5).upper()
        '''取毫秒级时间戳的后六位的十六进制表示数\n
        时间戳后六位 - 000000-999999        -> 0 - 16.67 Min\n
        五位十六进制 - 00000-FFFFF(1048575) -> 0 - 17.47 Min\n
        '''

        two_randint = str(random.randint(0,99)).zfill(2)

        self._ocn = timestamp + two_randint + str(self._count)
        
        return self._ocn

# ORDER_TIMEOUT

    def check_ocn(self, ocn):
        '''对返回的ocn进行分析检查'''
        if ocn == self._ocn:
            self._lock == True

    def __str__(self):
        return str(self.get_equipment_info())