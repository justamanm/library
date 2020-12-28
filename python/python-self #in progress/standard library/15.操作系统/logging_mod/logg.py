import logging
import os
import logging.config
import sys


class Log:
    def __init__(self):
        CONF_LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)),"config.ini")
        logging.config.fileConfig(CONF_LOG)  # 采用配置文件
        self.logger = logging.getLogger('zhejiang')


if __name__ == '__main__':
    logger = Log().logger
    logger.info("aasf")

