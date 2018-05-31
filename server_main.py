# Author: Janice Cheng

import socket
ip_port = ('127.0.0.1', 9999)

s = socket.socket()
s.bind(ip_port)
s.listen(5)

s_data = 'aaaaaaabbbbbbbbccccccccccdddddddddeeeeeeee'

while True:

    conn, addr = s.accept()

    while True:

        try:
            recv_data = conn.recv(1024)
            if len(recv_data) == 0:
                break

            send_data = recv_data.upper()
            print(send_data)

            conn.send(bytes(s_data, encoding='utf-8'))

        except Exception:
            break

    conn.close()
    print('close socket\n')

