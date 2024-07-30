储存函数运行返回结果的

用法:
```python
@result
def cfunc(a,b) -> int: # 事实上调用cfunc的时候func的返回值类型是Result
    return a/b
cfunc(10, 0).unwrap() # 使用 unwrap() 方法获取结果并且忽略错误,如果有错误,则会返回一个Exception
print(cfunc(10, 0)) # 使用 print() 方法打印结果,如果有错误,则会抛出异常
print(cfunc(10,2).extract()) # 使用 extract() 方法获取结果,如果有错误,则会抛出异常
```
或者不使用装饰器
```python
def cfunc(a,b) -> int:
    return a/b
cfunc = Result(cfunc)
cfunc.unwrap()
print(cfunc)
print(cfunc.extract())
```