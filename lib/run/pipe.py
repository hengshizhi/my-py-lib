from queue import Queue, Empty

class PipeClosedError(Exception):
    pass

class pipe_None:
    pass

class PQueue(Queue):
    closed = False
    def __init__(self):
        super().__init__()

    def __getattribute__(self, name):
        '''
        在每次方法调用之前检查队列是否关闭
        '''
        if name == 'closed':
            return object.__getattribute__(self, name)
        else:
            attr = super().__getattribute__(name)
            if object.__getattribute__(self, 'closed'):
                raise PipeClosedError("Pipe is closed")
            return attr
    
    def close(self):
        '''
        关闭队列
        '''
        while True:
            try:
                self.get(block=False)
            except Empty:
                break
        self.closed = True

class pipe_end:
    def __init__(self, name, my_queue: PQueue, his_queue: PQueue):
        self.name = name
        self.my_queue = my_queue
        self.his_queue = his_queue
        self.closed = False

    def send(self, data):
        if data is None:
            self.my_queue.put(pipe_None)
        else:
            self.my_queue.put(data)

    def recv(self):
        d = self.his_queue.get(block=False)
        if d == pipe_None:
            return None
        else:
            return d

    def try_recv(self) -> any:
        try:
            d = self.his_queue.get(block=False)
            if d == pipe_None:
                return None
            else:
                return d
        except Empty:
            return None

    def close(self):
        self.my_queue.close()
        self.his_queue.close()
    
def pipe(name=None) -> tuple[pipe_end,pipe_end]:
    my_queue = PQueue()
    his_queue = PQueue()
    return pipe_end(name,my_queue,his_queue), pipe_end(name,his_queue,my_queue)
