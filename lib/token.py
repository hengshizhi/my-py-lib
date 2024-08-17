'''
令牌接口标准库
'''
from abc import abstractmethod,ABC
from typing import TypeVar,Generic
from dataclasses import dataclass

Token = TypeVar('Token 的数据类型')
token_contains_data = TypeVar('Token 内含数据类型')
@dataclass
class New(ABC):
    '''
    新建的时候传入的数据
    '''
    token_token_contains_data:token_contains_data

@dataclass
class From(ABC):
    '''
    不新建的时候传入的数据
    '''
    token_data:Token

class token(ABC,Generic[token_contains_data]):
    def __init__(self) -> None:
        pass
    @abstractmethod
    def get(self) -> any:
        pass
    @abstractmethod
    def delete(self) -> None:
        pass
    @abstractmethod
    def set(self,value) -> None:
        pass
    @abstractmethod
    def production(self) -> Token:
        '''生成令牌,存放于客户端,并且使得这个令牌生效'''
        pass

    @abstractmethod
    @staticmethod
    def get_token_obj(data:New|From):
        '''
        用于验证token并且新建token对象和通过新的token数据新建token并且创建token对象
        '''
        pass

