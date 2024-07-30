from lib.run.queue import runQueue
from lib.run.pipe import pipe,pipe_end
from lib.run.task import task
from lib.run.task import run as task_run
from time import sleep
from abc import ABC, abstractmethod
class scheduling(ABC):
    def __init__(self) -> None:
        pass
    @abstractmethod
    def run(self) -> list[list[task]]:
        '''
        其返回值中,第一层list是同步运行的任务列表,意思就是在运行完index 0的所有任务之后就会运行index 1的任务,以此类推
        第二层list是异步运行的多个任务
        '''
        raise "请实现 run 方法"
    @abstractmethod
    def get(self,data:task_run):
        raise "请实现 get 方法"

class runing:
    def __init__(self,scheduling:scheduling,maximum_tasks_number:int,run_queue:runQueue,pipe_end:pipe_end,sleep_time) -> None:

        '''
        scheduling : scheduling 对象
        maximum_tasks_number : 最大任务数
        run_queue : 运行队列
        pipe_end : 管道
        sleep_time : 轮询间隔
        '''
        self.scheduling = scheduling
        self.maximum_tasks_number = maximum_tasks_number
        self.run_queue = run_queue
        self.pipe_end = pipe_end
        self.sleep_time = sleep_time
    def run_task(self):
        for tasks in self.scheduling.run():
            for return_ in [task.run(self.run_queue) for task in tasks]: # 运行所有的任务
                # print('逸已死吾亦死')
                return_.get()
                # print('逸已死吾亦死_疑惑')

    def run(self):
        '''
        运行调度线程主逻辑
        '''
        self.pipe_end.send(True) # 表示调度线程已经开始运行
        task_num = 0 # 任务数量
        old_task_data_is_None = True
        while True:
            task_data = self.pipe_end.try_recv()
            if task_data is None and old_task_data_is_None:
                self.run_task()
                old_task_data_is_None = False
                task_num = 0
            elif task_num >= self.maximum_tasks_number:
                self.run_task()
                old_task_data_is_None = False
                task_num = 0
            else:
                self.scheduling.get(task_data)
                old_task_data_is_None = True
                task_num += 1

            sleep(self.sleep_time) # 轮询间隔

class run:
    def __init__(self,scheduling:scheduling,maximum_tasks_number:int,run_queue:runQueue,sleep_time:any=0.1) -> None:
        self.p1,p2 = pipe()
        def runing_func():
            runing(scheduling,maximum_tasks_number,run_queue,p2,sleep_time).run()
        run_queue.put(runing_func)
        self.p1.recv() # 等待调度线程开始运行
    
    def plus(self,data:task):
        self.p1.send(data)
        return data.getobj