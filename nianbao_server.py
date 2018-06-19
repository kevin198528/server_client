from socket import *
import threading

# UDP socket

# max_size = 84*1024
#
# ip_port=('127.0.0.1', 8080)
# tcp_socket_server = socket(AF_INET,SOCK_DGRAM)
# tcp_socket_server.bind(ip_port)
# # tcp_socket_server.listen(5)
#
# # conn, addr = tcp_socket_server.accept()
# # data1 = conn.recv(10)
# # data2 = conn.recv(10)
#
# data1, address = tcp_socket_server.recvfrom(max_size)
#
#
# # print('----->', data1.dec)
# # conn.close()
#
# with open('./save/get_file_2.pdf', 'wb') as file:
#     file.write(data1)

RECV_SIZE = 100*1024*1024



# TCP socket
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    total_len = 0
    while True:
        data = sock.recv(RECV_SIZE)
        total_len = total_len + len(data)
        with open('./save/{}k'.format(int(len(data)/1024)), 'wb') as w_file:
            w_file.write(data)

        if len(data) is 0:
            print("disconnect")
            return
        print("data len:{} total len:{}".format(len(data), total_len))


ip_port = ("127.0.0.1", 8686)

s_tcp_server = socket(AF_INET, SOCK_STREAM)

s_tcp_server.bind(ip_port)

s_tcp_server.listen(5)

print("waiting for connection...")

while True:
    print("before accept")
    sock, addr = s_tcp_server.accept()
    print("after accept")
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
