import logging


class AutoLogger(object):
    def __init__(self,log_path,log_name):
        file_handler = logging.FileHandler(log_path, 'a', encoding='utf-8')
        fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
        file_handler.setFormatter(fmt)

        self.logger = logging.Logger(log_name, level=logging.DEBUG)
        self.logger.addHandler(file_handler)

    def log(self,msg):
        self.logger.error(msg)


logger = AutoLogger('cmdb.log','cmdb')