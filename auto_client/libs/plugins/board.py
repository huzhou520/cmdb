from .base import BasePlugin


class Board(BasePlugin):

    def process(self, hostname, ssh_func):
        ret = ssh_func(hostname, 'df -hT')
        # print(ret)
        return ret
