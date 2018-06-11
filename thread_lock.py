import threading, time, random

# self.tick_lock = threading.Lock()
#
# tick_lock.acquire()
#
# tick_lock.release()


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
