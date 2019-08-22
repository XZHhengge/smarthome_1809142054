# -*-coding:utf8-*-
import socket
import threading


def udp(data):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 定义成UDP
    # s.settimeout(10)  # socket发送和接收时间等待时间不能超过10秒

    ip_port = ('0.0.0.0', 23333)
    # ip_port = ('47.92.222.94', 5555)
    s.sendto(bytes(data.encode('utf-8')), ip_port)
    # ip_port = ('94.191.87.62', 23333)  # ip,端口
    while True:

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

if __name__ == '__main__':
    number = ['xxxxxxxxxxxxxxxxxxxxxxxxxxx', 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
        , 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb']
    for i in number:
        t = threading.Thread(target=udp, args=(i,))
        t.start()