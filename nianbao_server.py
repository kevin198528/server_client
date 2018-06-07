from socket import *

max_size = 64*1024

ip_port=('127.0.0.1', 8080)
tcp_socket_server = socket(AF_INET,SOCK_DGRAM)
tcp_socket_server.bind(ip_port)
# tcp_socket_server.listen(5)

# conn, addr = tcp_socket_server.accept()
# data1 = conn.recv(10)
# data2 = conn.recv(10)

data1, address = tcp_socket_server.recvfrom(max_size)


# print('----->', data1.dec)
# conn.close()

with open('./save/get_file_1.pdf', 'wb') as file:
    file.write(data1)
