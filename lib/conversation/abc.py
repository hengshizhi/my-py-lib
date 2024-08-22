from abc import ABC,abstractmethod
from typing import Callable

class ConversationalState(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def send(self, data):
        pass
    @abstractmethod
    def recv(self):
        pass
    @abstractmethod
    def try_recv(self) -> any:
        pass

class ConversationBase(ABC):
    def __init__(self,ConvState:ConversationalState) -> None:
        self.conv_funcs:dict = {}
        self.ConvState = ConvState

    def add(self,conv_id,processing_func):
        self.conv_funcs[conv_id] = processing_func