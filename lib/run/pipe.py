from queue import Queue

class pipe_None:pass

class pipe_end:
    def __init__(self, name,my_queue:Queue,his_queue:Queue):
        self.name = name
        self.my_queue = my_queue
        self.his_queue = his_queue
    def send(self, data):
        if data == None:
            self.my_queue.put(pipe_None)
        else:
            self.my_queue.put(data)
    def recv(self):
        d = self.his_queue.get()
        if d == pipe_None:
            return None
        else:
            return d
    def try_recv(self) -> any:
        try:
            return self.his_queue.get(block=False)
        except:
            return None
    
def pipe(name=None) -> tuple[pipe_end,pipe_end]:
    my_queue = Queue()
    his_queue = Queue()
    return pipe_end(name,my_queue,his_queue), pipe_end(name,his_queue,my_queue)
