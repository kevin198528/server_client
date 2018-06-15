import socket
import time, threading
import sys

from utils import *

cmd = {'bc_cmd': 'give_your_info'}
# must use jue dui path
root_path = "/home/zjq/PycharmProjects/server_client/server_client/"


def py_print(str):
    print("python: " + str)


class AbsDevice(object):
    def __int__(self, name):
        self.__name = name
        # self.__id = id


class Scanner(object):
    def __init__(self):
        print("scanner init")
        self.config = utils.load_config(root_path + "config/scanner.json")
        self.scan_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.scan_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # self.scan_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO)
        self.scan_socket.settimeout(0.1)
        self.ip_bc = self.config["ip_bc"]
        self.port_bc = self.config["port_bc"]
        self.addr_bc = (self.ip_bc, self.port_bc)
        self.rec_size = 5600
        self.dev_list = []

    def scanning(self):
        py_print("scanning start")
        self.scan_socket.sendto(utils.dict2json(cmd), self.addr_bc)

        for _ in range(10):
            try:
                data, addr = self.scan_socket.recvfrom(self.rec_size)
            except socket.timeout:
                print("socket receive from time out")
            else:
                name = data.decode('utf-8')
                self.dev_list.append(name)
                print(type(name))
                print(name)
                print(addr)

        py_print("scanning stop")
        print(self.dev_list)
        return self.dev_list


if __name__ == '__main__':
    # utils.utils
    # print(utils.__init__)
    # for t in sys.argv:
    #     print(t)
    #
    # print(sys.path)

    sc = Scanner()
    sc.scanning()
    # dev_monitor = DmMonitor(dev_info)
    # scanner_info = load_config("../config/scanner.json")
    # print(scanner_info)
