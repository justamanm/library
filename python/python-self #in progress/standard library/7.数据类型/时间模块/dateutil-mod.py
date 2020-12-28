import time
from datetime import datetime

# pip install python-dateutil
from dateutil.parser import parse


# 获取timedelta的时分秒
def delta2str():
    d1 = datetime.now()
    time.sleep(5)
    d2 = datetime.now()
    ret = d2 - d1

    date_ret = parse(str(ret))
    hour = date_ret.hour
    minute = date_ret.minute
    second = date_ret.second


# 时间字符戳转datetime类型
def str2datetime():
    ret = parse("2020-3-5")     # 2020-03-05 00:00:00
    print(ret)


if __name__ == '__main__':
    str2datetime()









