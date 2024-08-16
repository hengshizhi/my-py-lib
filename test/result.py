from lib.result import *

def ResultTest():
    def a(args, kwargs):
        return args[0]/args[1]
    _Result = Result(a, 10, 0)
    print(_Result)

def ResultTest2():
    @result
    def a(a,b) -> int:
        return a/b
    a(10, 0).unwrap() # 使用 unwrap() 方法获取结果并且忽略错误,如果有错误,则会返回一个Exception
    print(a(10, 0)) # 使用 print() 方法打印结果,如果有错误,则会抛出异常
    print(a(10,2).extract()) # 使用 extract() 方法获取结果,如果有错误,则会抛出异常


# ResultTest2()