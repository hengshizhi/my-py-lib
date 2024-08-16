'''
一个键值对数据库api
'''

from abc import abstractmethod
from .element import element
from typing import TypeVar,Generic

T = TypeVar('T')
class st(Generic[T]):
    @abstractmethod
    def __init__(self,db:dict,v_type:element) -> None:
        self.db = db
        self.v_type:element = v_type
    def put(self,k:bytes,v:T) -> None:
        self.db[k] = bytes(v)
    def del_k(self,k:bytes) -> None:
        del self.db[k]
    def get(self,k:bytes) -> T:
        ret = self.db.get(k)
        return None if ret == None else self.v_type(ret)

