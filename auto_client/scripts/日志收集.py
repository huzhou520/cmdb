import logging

"""
logging.basicConfig(filename='log.log',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=logging.DEBUG)

logging.debug('dd')
logging.error('err')
"""

file_handler = logging.FileHandler('cmdb.log', 'a', encoding='utf-8')
fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
file_handler.setFormatter(fmt)

logger = logging.Logger('cmdb', level=logging.DEBUG)
logger.addHandler(file_handler)

logger.error('dfdf')