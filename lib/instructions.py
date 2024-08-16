'''
指令模块，用于利用字符串执行指定python函数的解释器
'''
from typing import Callable

class null:pass

class call:
    def __init__(self,call_func:Callable[...,any],nedeargs:set[str]) -> None:
        '''
        call_func : 执行该指令时需要调用的函数
        nedeargs : 该指令需要参数名字的集合
        call_func 规定:
            如果其返回值为instructions.null 则运行之后就会返回instructions.null,否则会返回str,不是str将被强制转化为str
        '''
        self.nedes:set[str] = nedeargs
        self.func:Callable = call_func
    def run(self,nedeargs:dict[str,any]) -> any:
        ''''''
        return self.func(**nedeargs)


class instructions:
    def __init__(self,constant_args:dict[str,any]) -> None:
        '''
        constant_needs : 常量参数,意思就是在instructions实例化时就定好了的参数和其值
        '''
        self.__funcs:dict[str,call] = {}
        self.__constant_args:dict[str,any] = constant_args

    def add(self,name:str,func:call) -> None:
        self.__funcs[name] = func

    def del_func(self,name:str) -> None:
        del self.__funcs[name]

    def run_instructions(self,name:str,variables_args:dict[str,any]) -> str|null:
        '''
        variables_args : 变量参数,参数内容不固定的参数,同时其内容也可以覆盖常量参数
        '''
        call_obj = self.__funcs[name]
        call_nedes_set = call_obj.nedes
        args = self.__constant_args | variables_args
        call_nedes = {k:None for k in call_nedes_set} | {k:args[k] for k in call_nedes_set & set(args)}
        call_ret = call_obj.run(call_nedes)
        return str(call_ret) if call_ret == null else call_ret