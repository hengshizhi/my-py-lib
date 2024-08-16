用法示例:
```python
from lib.run.run import run # 调度线程类
from lib.run.scheduling import scheduling # 调度任务类的基类
from lib.run.task import task # 表示一个任务的任务类
from lib.run.task import run as task_run # 这个是在线程中的对象
from lib.run.queue import runQueue # runQueue 是一个队列,用于运行和储存任务

class _run(task_run):
    def run(self) -> any: # 在线程中会调用的函数
        import time
        print("info:",self.data) # self.data 是传给任务的参数
        for i in range(1):
            print(i)
            time.sleep(1)
        return 3 # 任务的运行结果
    
class _scheduling(scheduling):
    def __init__(self) -> None:
        self.snd = []
    def run(self) -> list[list[task]]: 
        # 调整任务的执行顺序, list的第一层是同步执行的,list第二层是并发的
        r = [[]]
        for i in self.snd:
            if i.runobj.data == 0:
                r.append([i])
            else:
                r[-1].append(i)

        # print(r)
        return r 
    def get(self,data:task): 
        # 每接收到一个任务就会执行这个,接收传入的任务
        self.snd.append(data)

r = run(_scheduling(),12,runQueue())
rs = []
for i in range(5):
    rs.append(r.plus(task(i%2,_run))) # 实例化task的时候第一个位置是参数,第二个位置是task_run

for i in rs:
    print(i.get()) # run.plus()返回的是task_run,task_run.get()返回的是任务执行的返回值
```