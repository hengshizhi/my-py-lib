from abc import ABC,abstractmethod
from typing import Callable,Awaitable,Type
from ..run.asyncio_pipe import PipeEnd,pipe
import asyncio

class ConnectingBase(ABC):
    @abstractmethod
    def __init__(self) -> None:pass
    @abstractmethod
    def send(self, data):pass
    @abstractmethod
    def recv(self):pass

class ConversationalStateBase:
    def __init__(self,pipe_end:PipeEnd,Connecting:ConnectingBase):
        self.pipe_end = pipe_end
        self.__Connecting = Connecting
    def send(self, data,*args,**kwrags):
        self.__Connecting.send( data,*args,**kwrags)
    async def recv(self) -> any:
        return await self.pipe_end.recv()
    async def try_recv(self) -> any:
        return await self.pipe_end.try_recv()

class ConversationBase(ABC):
    def __init__(self,ConvStateClass:Type[ConversationalStateBase],Connecting:ConnectingBase) -> None:
        '''
        ConvStateClass: 传入ConversationalState类(注意:是类,不是对象)
        Connecting: 传入Connecting对象
        '''
        self.conv_funcs:dict[any,Callable[[ConversationalStateBase],Awaitable[any]]] = {}
        self.ConvStateClass = ConvStateClass
        self.Connecting = Connecting

    def add(self,conv_id,processing_func:Callable[[ConversationalStateBase],Awaitable[any]]):
        '''
        conv_id : conv_id
        processing_func : 一个接受参数类型ConversationalState的异步函数
        '''
        self.conv_funcs[conv_id] = processing_func

    def __run_func(self):
        '''
        启动所有处理会话的函数
        '''
        self.conv_pipes:dict[any,PipeEnd] = {}
        for conv_id,processing_func in self.conv_funcs.items():
            pipe_a,pipe_b = pipe()
            self.conv_pipes[conv_id] = pipe_a
            asyncio.run(processing_func(self.ConvStateClass(pipe_b,self.Connecting)))

    def start_loop(self):
        '''
        开始事件循环
        '''
        self.__run_func()
        while True:
            the_conv_id,content = self.__sepa_id_and_content(self.Connecting.recv())
            asyncio.run(self.conv_pipes.get(the_conv_id).send(content))

    @abstractmethod
    def __sepa_id_and_content(self,data) -> tuple[any,any]:
        '''
        从获取的Connecting接收到的原始数据中解析出conv_id(会话id)和本次接收到的内容
        '''
        pass



