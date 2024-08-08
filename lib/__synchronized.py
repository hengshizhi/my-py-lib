import threading

def single_process(func):
    '''
    装饰器会使得被装饰的函数在同一进程的同一时刻只有一个实例在执行，其他实例会等待轮到自己执行
    '''
    lock = threading.Lock()

    def wrapper(*args, **kwargs):
        with lock:
            return func(*args, **kwargs)

    return wrapper


def synchronized_class(klass):
    '''
    可以确保一个类的所有方法都受到同一个锁的保护，实现方法级别的同步控制:
    示例用法
    >>> @synchronized_class
    >>> class SampleClass:
    >>>     def __init__(self):
    >>>         self.counter = 0
    >>>     def increment_counter(self):
    >>>         self.counter += 1
    >>>         return self.counter
    >>>     def multiply_counter(self, num):
    >>>         self.counter *= num
    >>>         return self.counter
    创建一个同步调用的类
    >>> synced_sample = SampleClass()
    测试同步调用
    >>> print(synced_sample.increment_counter())
    >>> print(synced_sample.multiply_counter(5))
    
    '''
    class WrappedClass(klass):
        _lock = threading.Lock()

        def __getattribute__(self, name):
            attr = super().__getattribute__(name)
            if callable(attr): # 如果是方法
                def synced_method(*args, **kwargs):
                    with self._lock:
                        return attr(*args, **kwargs)
                return synced_method
            return attr

    return WrappedClass
