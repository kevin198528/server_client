import socket
import time, threading
import sys

# root_path = "/home/zjq/PycharmProjects/server_client/server_client/"
# sys.path.append(root_path)

from utils import *

# from ../utils import *
#
# from uti

cmd = {'bc_cmd': 'give_your_info'}
# must use jue dui path


def py_print(str):
    print("python: " + str)


class AbsDevice(object):
    def __init__(self, name):
        self.__name = name
        # self.__id = id

    def get_name(self):
        return self.__name


class Scanner(object):
    def __init__(self):
        print("scanner init")
        self.config = utils.load_config("/home/zjq/PycharmProjects/server_client/config/scanner.json")
        self.scan_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.scan_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # self.scan_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO)
        self.scan_socket.settimeout(0.05)
        self.ip_bc = self.config["ip_bc"]
        self.port_bc = self.config["port_bc"]
        self.addr_bc = (self.ip_bc, self.port_bc)
        self.rec_size = 5600

    def scanning(self):
        py_print("scanning start")
        self.dev_list = []
        self.scan_socket.sendto(utils.dict2json(cmd), self.addr_bc)

        for _ in range(12):
            try:
                data, addr = self.scan_socket.recvfrom(self.rec_size)
            except socket.timeout:
                print("socket receive from time out")
            else:
                name = data.decode('utf-8')
                py_print(name)
                camera_dev = AbsDevice(name)
                self.dev_list.append(camera_dev)
                print(type(name))
                print(name)
                print(addr)

        print(self.dev_list)
        py_print("scanning stop")
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
