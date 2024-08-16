import threading
from queue import Queue

class CustomThread(threading.Thread):
    def __init__(self, queue, **kwargs):
        super(CustomThread, self).__init__(**kwargs)
        self.__queue = queue

    def run(self):
        while True:
            item = self.__queue.get()[0]
            try:
                item[0](*item[1:])
            except TypeError:
                item()
            self.__queue.task_done()

class runQueue:
    def __init__(self,ThreadSize=10) -> None:
        self.ThreadS = []
        self.q = Queue()
        for _ in range(ThreadSize):
            t = CustomThread(self.q, daemon=True)
            t.start()
            self.ThreadS.append(t)

    def join(self):
        self.q.join()
    
    def put(self, func, *args):
        self.q.put((func, *args))
