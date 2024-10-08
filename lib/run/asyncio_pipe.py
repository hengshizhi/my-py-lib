from typing import Any, Optional, Tuple
from asyncio import Queue as AsyncQueue
from asyncio import QueueEmpty
from .pipe import PipeClosedError

PipeNone = object()

class PQueue(AsyncQueue):
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
                self.get_nowait()
            except QueueEmpty:
                break
        self.closed = True

class PipeEnd:
    def __init__(self, name: Optional[str], my_queue: PQueue, his_queue: PQueue):
        self.name = name
        self.my_queue = my_queue  
        self.his_queue = his_queue

    async def send(self, data: Any):
        """
        将数据发送到另一端的队列中
        """
        if data == None:
            await self.his_queue.put(PipeNone)
        else:
            await self.his_queue.put(data)

    async def recv(self) -> Any:
        """
        从队列中获取数据
        """
        d = await self.my_queue.get()
        return None if d is PipeNone else d

    async def try_recv(self) -> Optional[Any]:
        """
        尝试从队列中获取数据,如果队列为空则返回None
        """
        try:
            return await self.my_queue.get_nowait()
        except QueueEmpty:
            return None

    async def close(self):
        self.my_queue.close()
        self.his_queue.close()

def pipe(name: Optional[str] = None) -> Tuple[PipeEnd, PipeEnd]:
    """
    创建一个双向管道,包含两个PipeEnd实例
    """
    my_queue = PQueue()
    him_queue = PQueue()
    return PipeEnd(name, my_queue, him_queue), PipeEnd(name, him_queue, my_queue)