import threading
from lib.run.queue import runQueue
def __main_test():
    q = runQueue()
    import time
    import random

    taskId =  1
    # 模拟任务耗时(秒)
    consuming = random.randint(1, 5)
    


    def task(taskId, consuming,func):
        thread_name = threading.current_thread().getName()
        print('工人【%s】正在处理任务【%d】：do something...' % (thread_name, taskId))
        # 模拟任务耗时(秒)
        time.sleep(consuming)
        print('任务【%d】：done' % taskId)
        if taskId >= 10:
            print('队列已处理完所有任务')
            return 0
        taskId = taskId + 1
        # 模拟任务耗时(秒)
        consuming = random.randint(1, 5)
        q.put((func, taskId, consuming,func))
        def ___1(taskId, consuming):
            thread_name = threading.current_thread().getName()
            print('\n工人【%s】正在处理任务【%d】114514aaaa：do something...' % (thread_name, taskId))
        q.put((___1, taskId, consuming))
        

    q.put((task, taskId, consuming,task))
    # 阻塞队列

    q.join()