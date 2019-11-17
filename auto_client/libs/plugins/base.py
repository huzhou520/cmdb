class BasePlugin(object):
    def process(self, hostname, ssh_func):
        raise NotImplementedError(f'该类{self.__class__.__name__}必须要有process方法。')


# 数据类型的封装
class BaseResponse(object):
    def __init__(self):
        self.status = True
        self.data = None
        self.error = None

    @property
    def dic(self):
        return self.__dict__

