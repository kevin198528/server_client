
# print('process {} start...'.format(os.getpid()))
#
# pid = os.fork()
#
# if pid == 0:
#     print('i am child process {} parent pid is {}'.format(os.getpid(), os.getppid()))
# else:
#     print('i am father process {} child pid is {}'.format(os.getpid(), pid))

import threading, time
from devices.module_test import *

# class MyThread2(threading.Thread):
#     def __init__(self, id):
#         threading.Thread.__init__(self)
#         self.id = id
#
#     def run(self):
#         print('start:' + str(self.id))
#         time.sleep(5)
#         print('end:' + str(self.id))
#
#
# class MyThread(threading.Thread):
#     def __init__(self, id):
#         threading.Thread.__init__(self)
#         self.id = id
#
#     def run(self):
#         print('start:' + str(self.id))
#         t2 = MyThread2(2)
#         t2.setDaemon(True)
#         t2.start()
#         time.sleep(2)
#         print('end:' + str(self.id))

# def MyThread(threa):
#
#
# def run_proc(*a, **b):
#     time.sleep(1)
#     print('process{} is {} and {}'.format(os.getpid(), a, b))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, kwargs={'a': 123, 'b': 456}, args=['1', '2'])
#     print('Child process will start.')
#     p.start()
#     p.join()
#
#     print('Child process end.')

# class Animal(object):
#     def __init__(self, name):
#         self.name = name
#
#     def greet(self):
#         print('Hello, I am %s.' % self.name)
#
#
# class Dog(Animal):
#     def greet(self):
#         # super(Dog, self).greet()  # Python3 可使用 super().greet()
#         print(id(Animal.greet(self)))
#         print(id(super(Dog, self).greet()))
#         print(id(super().greet()))
#
#         print('WangWang...')


class asd(object):
    def __new__(cls, *args, **kwargs):
        print("cls id {}".format(cls))
        print("cls id {}".format(id(cls)))
        r = super(asd, cls).__new__(cls)
        print("r id {}".format(r))
        print("r id {}".format(id(r)))
        return r


class bnm(asd):
    def __init__(self, name):
        print("bnm self id {}".format(id(self)))
        self.name = name

o = bnm('name')


print("asd is {}".format(id(asd)))
print("asd is {}".format(asd))
print("bnm is {}".format(id(bnm)))
print("asd is {}".format(bnm))
print("o is {}".format(id(o)))