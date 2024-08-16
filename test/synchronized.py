from lib import synchronized_class

@synchronized_class
class SampleClass:
    def __init__(self):
        self.counter = 0

    def increment_counter(self):
        self.counter += 1
        return self.counter

    def multiply_counter(self, num):
        self.counter *= num
        return self.counter

# 创建一个同步调用的类
synced_sample = SampleClass()

# 测试同步调用
print(synced_sample.increment_counter())
print(synced_sample.multiply_counter(5))