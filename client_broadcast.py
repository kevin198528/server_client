import socket
import subprocess  # 执行命令模块

# udp_gb_client.py
'''客户端（UDP协议局域网广播）'''

import socket

IP = ''
PORT = 6363
max_size = 65535


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

s.bind((IP, PORT))
print('Listening for broadcast at ', s.getsockname())

while True:
    data, address = s.recvfrom(max_size)
    print('Server received from {}:{}'.format(address, data.decode('utf-8')))
    s.sendto('deviceAAAAA'.encode('utf-8'), address)
