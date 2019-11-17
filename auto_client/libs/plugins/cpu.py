from .base import BasePlugin
import traceback
from libs.log import logger


class Cpu(BasePlugin):
    def process(self, hostname, ssh_func):
        # 定义数据格式
        info = {"status": True, "data": None, "error": None}

        try:
            # 远程从服务器执行命令取出结果给ret
            ret = ssh_func(hostname, 'cat /proc/cpuinfo | head -n 4')
            # 对结果ret进行过滤处理
            parse_ret = self.parse(ret)
            info["data"] = parse_ret
        except Exception as e:
            msg = traceback.format_exc()
            logger.log(msg)
            info["status"] = False
            info["data"] = msg

        # print(parse_ret)
        return info

    def parse(self, content):
        data_dict = {}
        list_data = content.strip().split('\n')
        print(list_data, 'cpu文件')
        # list_data.pop()
        for value in list_data:
            # if not value:
            #     continue

            k, v = value.split(':')
            # print(k.strip(), v)
            data_dict[k.strip()] = v
        return data_dict
