import os, time
from multiprocessing import Process

# print('process {} start...'.format(os.getpid()))
#
# pid = os.fork()
#
# if pid == 0:
#     print('i am child process {} parent pid is {}'.format(os.getpid(), os.getppid()))
# else:
#     print('i am father process {} child pid is {}'.format(os.getpid(), pid))


def run_proc(*a, **b):
    time.sleep(1)
    print('process{} is {} and {}'.format(os.getpid(), a, b))


if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, kwargs={'a': 123, 'b': 456}, args=['1', '2'])
    print('Child process will start.')
    p.start()
    p.join()

    print('Child process end.')