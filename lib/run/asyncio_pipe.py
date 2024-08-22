from typing import Any, Optional, Tuple
from queue import Queue as SyncQueue
from asyncio import Queue as AsyncQueue
from asyncio import QueueEmpty

PipeNone = object()

class PipeEnd:
    def __init__(self, name: Optional[str], my_queue: AsyncQueue, his_queue: AsyncQueue):
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

def pipe(name: Optional[str] = None) -> Tuple[PipeEnd, PipeEnd]:
    """
    创建一个双向管道,包含两个PipeEnd实例
    """
    my_queue = AsyncQueue()
    him_queue = AsyncQueue()
    return PipeEnd(name, my_queue, him_queue), PipeEnd(name, him_queue, my_queue)