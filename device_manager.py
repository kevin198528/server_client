import socket
import time, threading
import json

dev_info = {
    'cmd_info': {
      'ip': '127.0.0.1',
      'port': 6383,
      'type': 'udp'
    },
    'stream_info': {
      'ip': '127.0.0.1',
      'port': 6386,
      'type': 'tcp'
    }
}


class DmBroadcastor(object):
    def __init__(self):
        pass


class DmMonitor(object):
    def __init__(self, dev_info):
        self.__json_dev_info = json.dumps(dev_info)

        self.__m_thread = None
        self.__ip = ''
        self.__port = 6363
        self.__max_size = 65535
        self.__s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.__s.bind((self.__ip, self.__port))

        print('device manager - monitor - Listening for broadcasting', self.__s.getsockname())

        self.__m_thread = threading.Thread(target=self.monitor_thread_loop, name='monitor_thread_loop')

        self.__m_thread.start()
        self.__m_thread.join()

    def monitor_thread_loop(self):
        while True:
            utf8_data, address = self.__s.recvfrom(self.__max_size)

            data = json.loads(utf8_data.decode('utf-8'))

            print(data)

            if data['cmd'] == 'get_dev_info':
                print('send dev info to {}'.format(address))
                self.__s.sendto(self.__json_dev_info.encode('utf-8'), address)
            # print('Server received from {}:{}'.format(address, data.decode('utf-8')))


if __name__ == '__main__':
    print('main')
    dev_monitor = DmMonitor(dev_info)
