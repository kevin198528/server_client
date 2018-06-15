import threading, time, random

# self.tick_lock = threading.Lock()
#
# tick_lock.acquire()
#
# tick_lock.release()

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

class GThread(threading.Thread):
    tick_lock = threading.Lock()
    ticks = 100
    bought_ticks = 0

    def __init__(self):
        # print(self.name)
        print(id(self))
        threading.Thread.__init__(self)
        print('G')


class AThread(GThread):
    def __init__(self, tid):
        # GThread.__init__(self)
        # super.__i
        print(id(self))
        super().__init__()
        self.tid = tid


    def run(self):

        while True:
            with GThread.tick_lock:
                if GThread.ticks > 0:
                    print('{} left ticks:'.format(self.tid) + str(self.ticks))
                    time.sleep(0.01)
                    GThread.ticks -= 1
                    GThread.bought_ticks += 1
                else:
                    return


class BThread(GThread):
    def __init__(self):
        GThread.__init__(self)
        self.id = 'B thread'

    def run(self):
        while True:
            if self.ticks > 0:
                print('B thread ticks:' + str(self.ticks))

            time.sleep(2)
            GThread.ticks -= 1


if __name__ == "__main__":
    thread_pool = []
    # for i in range(10):
    #     tmp = AThread(i)
    #     thread_pool.append(tmp)
    #
    # for t in thread_pool:
    #     t.start()
    #
    # for t in thread_pool:
    #     t.join()

    tmp = AThread(1)

    # tmp.start()

    print(type(tmp))

    # print('end')
    # print('g left ticks:{}'.format(GThread.ticks))
    # print('g bought ticks:{}'.format(GThread.bought_ticks))
