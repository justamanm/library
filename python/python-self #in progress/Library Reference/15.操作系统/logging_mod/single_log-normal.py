import logging
import os
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger("single_log")  # 不加名称设置root logger
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "[%(asctime)s] %(levelname)s in %(filename)s[%(lineno)d]: 》 %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S')

# 使用StreamHandler输出到屏幕
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
sh.setFormatter(formatter)

# 使用FileHandler输出到文件
fh = logging.FileHandler('./log/log.txt', encoding="utf8")
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

# 按照时间间隔分隔日志文件
# TimedRotatingFileHandler(filename [,when [,interval [,backupCount]]])
# when-时间单位：S-seconds,M-minute,H-hour,D-day,W-week(0-6),midnight-每天0点
# interval-指定单位的间隔
# 如：when="D",interval=3；每3天创建一个新日志文件；当是W时，要指定interval，为0表示每周一，1-每周二
# backupCount保留几个：默认的0是不会自动删除掉日志，若设10，则在文件的创建过程中库会判断是否有超过这个10，若超过，则会从最先创建的开始删除
# 代码：
filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log/log.txt")
th = TimedRotatingFileHandler(filename=filename, when="D", interval=30, backupCount=5, encoding='utf-8')
th.setLevel(logging.DEBUG)
th.setFormatter(formatter)

# 添加Handler
logger.addHandler(sh)
logger.addHandler(th)
logger.info('this is info message')
logger.warning('this is warn message')
