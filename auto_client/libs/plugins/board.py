import traceback
from .base import BasePlugin
from libs.log import logger
import settings


class Board(BasePlugin):

    def process(self,hostname,ssh_func):
        """
        执行命令，去获取主板
        :return:
        """
        info = {'status': True, 'data': None, 'error': None}
        try:

            if settings.DEBUG:
                with open('files/board.out', mode='r', encoding='utf-8') as f:
                    content = f.read()
            else:
                content = ssh_func(hostname, 'sudo dmidecode -t1')
            data = self.parse(content)
            info['data'] = data
        except Exception as e:
            msg = traceback.format_exc()
            logger.log(msg)
            info['status'] = False
            info['error'] = msg
        return info

    def parse(self, content):

        result = {}
        key_map = {
            'Manufacturer': 'manufacturer',
            'Product Name': 'model',
            'Serial Number': 'sn',
        }

        for item in content.split('\n'):
            row_data = item.strip().split(':')
            if len(row_data) == 2:
                if row_data[0] in key_map:
                    result[key_map[row_data[0]]] = row_data[1].strip() if row_data[1] else row_data[1]

        return result
