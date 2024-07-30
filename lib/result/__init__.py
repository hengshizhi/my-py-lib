from typing import TypeVar,Generic,Callable

T = TypeVar('T')

class Result(Generic[T]): # 定义泛型
    '''
    类型表达式 : Result[OK Type]
    '''
    class OK:
        def __init__(self,message):
            self.message = message
        def __str__(self) -> str:
            return "OK: " + str(self.message)

    def __init__(self,func,*args, **kwargs ):
        self.__run__(func,args,kwargs)
        
    def __str__(self):
        if self.__code__ == True:
            return str(self.OK(self.__result_data__))
        else:
            raise self.__error_message__
    
    def __run__(self, func, args:list, kwargs:dict) -> bool:
        self.__result_data__ = bytes()
        try:
            self.__result_data__ = func(*args, **kwargs)
            self.__code__ = True
            return True
        except Exception as e:
            self.__error_message__ = e
            self.__code__ = False
            return False

    def __hash__(self) -> int:
        return hash(str(self.__result_data__) + str(self.__error_message__) + str(self.__code__))

    def to_string(self):
        self.__str__()
    
    def unwrap(self):
        if self.__code__ == True:
            return self.__result_data__
        else:
            # raise self.__error_message__
            return self.__error_message__
        
    def extract(self):
        if self.__code__ == True:
            return self.__result_data__
        else:
            raise self.__error_message__
        
    def is_OK(self):
        return self.__code__
    
    def is_error(self):
        return not self.__code__


def result(func:Callable[..., T]) -> Callable[..., Result[T]]:
    return lambda *args, **kwargs:Result(func,*args, **kwargs)

