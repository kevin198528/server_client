import socket

BUFSIZE=1024
ip_port=('127.0.0.1',8080)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# res = s.connect_ex(ip_port)

with open('./img/41k.png', 'rb') as file:
    read_file = file.read()

    print(len(read_file))

    s.sendto(read_file, ip_port)

# s.send('hello'.encode('utf-8'))
# s.send('feng'.encode('utf-8'))