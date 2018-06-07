# Author: Janice Cheng

import socket

ip_port = ('127.0.0.1', 9999)
s = socket.socket()
s.connect(ip_port)

while True:
    send_data = input(">>: ").strip()
    if len(send_data) == 0:
        print('continue len:' + str(len(send_data)))
        continue

    print('len:' + str(len(send_data)))

    s.send(bytes(send_data, encoding='utf8'))

    if send_data == 'exit':
        break

    recv_data = s.recv(10)
    print(str(recv_data, encoding='utf8'))
    recv_data = s.recv(10)
    print(str(recv_data, encoding='utf8'))
    recv_data = s.recv(10)
    print(str(recv_data, encoding='utf8'))

s.close()
