from .base import BasePlugin
from .base import BaseResponse
import re
import traceback
from libs.log import logger


class Disk(BasePlugin):
    def process(self, hostname, ssh_func):
        # info = {'status': True, 'data': None, 'error': None}
        info = BaseResponse()
        try:
            with open('files/disk_out', mode='r') as f1:
                content = f1.read()
            # ret = ssh_func(hostname, "df -hTi")

            parse_ret = self.parse(content)
            # info['data'] = parse_ret
            info.data = parse_ret

        except Exception as e:
            # info['status'] = False
            info.status = False
            msg = traceback.format_exc()
            logger.log(msg)
            # info['error'] = msg
            info.error = msg

        return info.dic

    def parse(self, content):
        """
        解析shell命令返回结果
        :param content: shell 命令结果
        :return:解析后的结果
        """
        response = {}
        result = []
        for row_line in content.split("\n\n\n\n"):
            result.append(row_line)
        for item in result:
            temp_dict = {}
            for row in item.split('\n'):
                if not row.strip():
                    continue
                if len(row.split(':')) != 2:
                    continue
                key, value = row.split(':')
                name = self.mega_patter_match(key)
                if name:
                    if key == 'Raw Size':
                        raw_size = re.search('(\d+\.\d+)', value.strip())
                        if raw_size:
                            temp_dict[name] = raw_size.group()
                        else:
                            raw_size = '0'
                    else:
                        temp_dict[name] = value.strip()
            if temp_dict:
                response[temp_dict['slot']] = temp_dict
        return response

    @staticmethod
    def mega_patter_match(needle):
        grep_pattern = {'Slot': 'slot', 'Raw Size': 'capacity', 'Inquiry': 'model', 'PD Type': 'pd_type'}
        for key, value in grep_pattern.items():
            if needle.startswith(key):
                return value
        return False