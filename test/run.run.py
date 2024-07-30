from lib.run.run import scheduling,run


def test():
    '''
    同步运行测试
    '''
    from lib.run.task import task
    from lib.run.task import run as task_run
    from lib.run.queue import runQueue

    class _run(task_run):
        def run(self) -> any:
            import time
            print("info:",self.data)
            for i in range(10):
                print(i)
                time.sleep(1)
            return 3
        
    class _scheduling(scheduling):
        def __init__(self) -> None:
            self.snd = []
        def run(self) -> list[list[task]]:
            r = [[i] for i in self.snd]
            self.snd = []
            return r
        def get(self,data):
            self.snd.append(data)

    r = run(_scheduling(),12,runQueue())
    r.plus(task(1,_run))
    r.plus(task(2,_run))
    r.plus(task(3,_run)).join()

# test()
    
def test1():
    '''
    异步运行测试
    '''
    from lib.run.task import task
    from lib.run.task import run as task_run
    from lib.run.queue import runQueue

    class _run(task_run):
        def run(self) -> any:
            import time
            print("info:",self.data)
            for i in range(10):
                print(i)
                time.sleep(1)
            return 3
        
    class _scheduling(scheduling):
        def __init__(self) -> None:
            self.snd = []
        def run(self) -> list[list[task]]:
            r = [[i for i in self.snd]]
            self.snd = []
            return r
        def get(self,data):
            self.snd.append(data)

    r = run(_scheduling(),12,runQueue())
    r.plus(task(1,_run))
    r.plus(task(2,_run))
    r.plus(task(3,_run)).join()

# test1()
    
def test1():
    '''
    异步同步混合运行测试
    '''
    from lib.run.task import task
    from lib.run.task import run as task_run
    from lib.run.queue import runQueue

    class _run(task_run):
        def run(self) -> any:
            import time
            print("info:",self.data)
            for i in range(1):
                print(i)
                time.sleep(1)
            return 3
        
    class _scheduling(scheduling):
        def __init__(self) -> None:
            self.snd = []
        def run(self) -> list[list[task]]:# 分配任务
            r = [[]]
            for i in self.snd:
                if i.runobj.data == 0:
                    r.append([i])
                else:
                    r[-1].append(i)

            # print(r)
            return r 
        def get(self,data:task):
            self.snd.append(data)

    r = run(_scheduling(),12,runQueue())
    rs = []
    for i in range(5):
        rs.append(r.plus(task(i%2,_run)))

    for i in rs:
        print(i.get())
# test1()
