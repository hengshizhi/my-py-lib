from lib.run.queue import runQueue
from lib.run.task import task,run

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