class Single(object):
    instance = None
    def __init__(self):
        self.name = 'zhuzhu'

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = object.__new__(cls)
        return cls.instance

obj = Single()
obj2 = Single()
print(obj.name)
print(obj2.name)

# 单例模式二：
import threading

class SingleTon(object):
    instance = None
    lock = threading.RLock()

    def __new__(cls, *args, **kwargs):
        if cls.instance:
            return cls.instance
        with cls.lock:
            if not cls.instance:
                cls.instance = object.__new__(cls)
            return cls.instance

obj1 = SingleTon()
obj2 = SingleTon()
print(obj1, obj2, sep="\n")

# class SingleT(object):
#     instance = None
#     lock = threading.RLock()
#
#     def __new__(cls, *args, **kwargs):
#         if cls.instance:
#             return cls.instance
#         with cls.lock:
#             if not cls.instance:
#                 cls.instance = super().__new__(cls)
#             return cls.instance

"""
xx.py
def A():
    print(111)
site = A()

#################

import xx
print(xx.site)
"""

