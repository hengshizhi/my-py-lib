from lib.run.pipe import pipe
import time

def test():
    p1,p2 = pipe("test")
    p1.send("hello")
    print(p2.recv())

def test2():
    p1,p2 = pipe("test")
    # while True:
    #     # p1.send("hello")
    #     print(p1.try_recv())

# test2()