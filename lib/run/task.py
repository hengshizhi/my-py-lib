from lib.run.pipe import pipe_end,pipe
from lib.run.queue import runQueue
from threading import Lock
from abc import abstractmethod

class run:
    def __init__(self,data,pipe_end:pipe_end):
        self.data=data
        self.pipe_end=pipe_end
    def return_data(self,data):
        self.pipe_end.send(data)
    @abstractmethod
    def run(self) -> any:pass

class get_return_data:
    class no_get_return_data :pass
    start_runing = False # 是否开始运行
    return_data = no_get_return_data # 返回的数据
    def __init__(self,pipe_end:pipe_end):
        self.pipe_end=pipe_end
        self.Lock = Lock() # 线程锁

    def _get(self) -> any:
        '''
        第一次收到数据为self.start_runing = True
        第二次收到数据为self.return_data = 数据
        '''
        if bool(self.start_runing):
            return self.return_data
        elif self.return_data == self.no_get_return_data:
            self.return_data = self.pipe_end.recv()
            return self._get()
        else:
            self.start_runing = True
            return self._get()

    
    def get(self) -> any:
        '''获取返回数据'''
        with self.Lock: # 只允许一处获取数据
            d = self._get()
        return d

    def _try_get(self) -> any:
        '''
        尝试获取数据
        '''
        data = self.pipe_end.try_recv()
        if data:
            if self.start_runing:
                self.return_data = data
                return data
            else:
                self.start_runing = True
                return None
        return None
    
    def try_get(self) -> any:
        '''尝试获取返回数据'''
        with self.Lock: # 只允许一处获取数据
            return self._try_get()

    def join(self):
        self.get()

class task:
    def __init__(self,run_data,run_class:run,get_return_data_class:get_return_data = get_return_data ,name=None) -> None:
        '''
        run_data: 运行时所需要的数据
        '''
        p1,p2 = pipe(name)
        self.runobj = run_class(run_data,p1)
        self.get_p = p2
        self.getobj = get_return_data_class(p2)
    
    def run(self,queue:runQueue) -> get_return_data:
        def run_task(get_p,runobj):
            get_p.send(True) # 任务开始运行
            runobj.return_data(self.runobj.run())
        queue.put((run_task,self.get_p,self.runobj))
        return self.getobj

def test():
    import time
    class _run(run):
        def run(self) -> any:
            print("info:",self.data)
            for i in range(10):
                print(i)
                time.sleep(1)
            return 3
    run_q = runQueue()
    _task = task(1,_run)
    _task.run(run_q)
    _task = task(1,_run)
    _task.run(run_q)
    _task.getobj.join()
    print(_task.getobj.get())
    
# test()