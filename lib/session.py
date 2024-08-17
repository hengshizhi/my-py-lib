'''
一个用于表示状态的会话接口标准库
'''
from abc import abstractmethod,ABC
from typing import TypeVar,Generic
from dataclasses import dataclass
@dataclass
class New(ABC):
    '''
    新建的时候传入的数据
    '''
    pass

@dataclass
class From(ABC):
    '''
    不新建的时候传入的数据
    '''
    pass

T = TypeVar('会话数据键格式')
B = TypeVar('会话数据格式')
class session(ABC,Generic[T],Generic[B]):
    '''
    session[会话数据键格式,会话数据格式]
    '''
    @abstractmethod
    def __init__(self,data:New|From) -> None:
        pass
    @abstractmethod
    def get(self,field:T) -> B:
        pass
    @abstractmethod
    def del_field(self,field:T) -> None:
        pass
    @abstractmethod
    def put(self,field:T,val:B) -> None:
        pass
    @abstractmethod
    def to_store_media(self) -> any:
        '''转变为其他储存介质的重要手段'''
        pass