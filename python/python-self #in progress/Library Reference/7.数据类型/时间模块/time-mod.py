import time


t1 = time.time()     # 返回时间戳，即从1970.01.01到现在的秒数
print(t1)

t2 = time.localtime()    # 返回time.struct_time(tm_year=2016, tm_mon=4, tm_mday=7, tm_hour=10,...)
print(t2)

time.strftime("")     # 将时间类型转换为字符串

time.strptime("")     # 将字符串转换为时间类型


