# Chức năng chính : Sử dụng socket để quét các cổng trên một máy chủ, để xác định xem cổng đó có mở hay không.

import socket

# IP cần quét
target = '172.16.0.190'

def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        return True
    except:
        return False

for p in range(1, 1025):
    result = portscan(p)
    if result:
        print('Port {} is open'.format(p))
    else:
        print('Port {} is closed'.format(p))
