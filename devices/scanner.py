import socket
import time, threading
from utils.utils import *


#
# dev_info = {
#     'cmd_info': {
#       'ip': '127.0.0.1',
#       'port': 6383,
#       'type': 'udp'
#     },
#     'stream_info': {
#       'ip': '127.0.0.1',
#       'port': 6386,
#       'type': 'tcp'
#     }
# }


# class DmBroadcastor(object):
#     def __init__(self):
#         pass
#
#
# class DmMonitor(object):
#     def __init__(self, dev_info):
#         self.__json_dev_info = json.dumps(dev_info)
#
#         self.__m_thread = None
#         self.__ip = ''
#         self.__port = 6363
#         self.__max_size = 65535
#         self.__s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         # s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#         self.__s.bind((self.__ip, self.__port))
#
#         print('device manager - monitor - Listening for broadcasting', self.__s.getsockname())
#
#         self.__m_thread = threading.Thread(target=self.monitor_thread_loop, name='monitor_thread_loop')
#
#         self.__m_thread.start()
#         self.__m_thread.join()
#
#     def monitor_thread_loop(self):
#         while True:
#             utf8_data, address = self.__s.recvfrom(self.__max_size)
#
#             data = json.loads(utf8_data.decode('utf-8'))
#
#             print(data)
#
#             if data['cmd'] == 'get_dev_info':
#                 print('send dev info to {}'.format(address))
#                 self.__s.sendto(self.__json_dev_info.encode('utf-8'), address)
#             # print('Server received from {}:{}'.format(address, data.decode('utf-8')))

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#
# PORT = 6363
#
# network = '<broadcast>'
#
# cmd = {'cmd': 'get_dev_info'}
#
# json_cmd = json.dumps(cmd)
#
# s.sendto(json_cmd.encode('utf-8'), (network, PORT))
#
# data, address = s.recvfrom(5600)

cmd = {'bc_cmd': 'give_your_info'}


def py_print(str):
    print("python: " + str)


class Scanner(object):
    def __init__(self):
        self.config = load_config("../config/scanner.json")
        py_print("scanner create")
        self.scan_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.scan_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # self.scan_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO)
        self.scan_socket.settimeout(1)
        self.ip_bc = self.config["ip_bc"]
        self.port_bc = self.config["port_bc"]
        self.addr_bc = (self.ip_bc, self.port_bc)
        self.rec_size = 5600


    def scanning(self):
        py_print("scanning start")
        self.scan_socket.sendto(dict2json(cmd), self.addr_bc)
        try:
            data, addr = self.scan_socket.recvfrom(self.rec_size)
        except socket.timeout:
            print("socket receive from time out")
        else:
            print(data)
            print(addr)
        # time.sleep(2)
        py_print("scanning stop")


if __name__ == '__main__':
    sc = Scanner()
    sc.scanning()
    # dev_monitor = DmMonitor(dev_info)
    # scanner_info = load_config("../config/scanner.json")
    # print(scanner_info)



