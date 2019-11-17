class BaseResponse(object):
    def __init__(self):
        self.status = True
        self.data = None
        self.error = None

    @property
    def dict(self):
        return self.__dict__


def process():
    info = BaseResponse()
    try:
        info.status = True
        info.data = 'Data is enough'
    except Exception as e:
        print('错误')
    return info.dict
