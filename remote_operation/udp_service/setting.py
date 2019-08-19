# -*-coding:utf-8-*-

'''localhost UDPServer地址
HB_INITCOUNT 心跳包初始计数
HB_REDUCTION 心跳包计数减少量
'''


LOCAL_HOST = ('0.0.0.0', 23333) 
'''UDPServer地址'''

ORDER_TIMEOUT = 3
'''指令超时时间,向设备发送的指令的超时时间(s),只能为整数
准确来说是两条指令的发送间隔,因为发送出的指令虽然超时但可能已经成功送达
'''

HB_INITCOUNT = 300
'''心跳包初始计数'''

HB_REDUCTION = 10
'''心跳包计数减少量'''

HB_REDUCTIONRATE = 10
'''心跳包递减间隔(s)'''