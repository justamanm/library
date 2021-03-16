import time
from datetime import datetime, timedelta, date
from datetime import time as date_time
import datetime as dt

# datetime模块下：
# date类，年月日
# time类，时分秒
# datetime类(继承自date)
# timedelta，日期加减(datetime类型和date类型相减都是timedelta)


class DateStr:
    def create_date(self):
        # import datetime
        # date = datetime.date(2020, 7, 20)
        date = dt.date(2020, 7, 20)
        date1 = dt.date(2019, 6, 10)
        # year = date.year
        # month= date.month
        # day = date.day
        # date.today()
        # date.weekday()
        # date.toordinal()
        print(type(date - date1))

    def str2date(self):
        date_str = "2020-07-20"
        str_list = date_str.split("-")
        ret = dt.date(int(str_list[0]), int(str_list[1]), int(str_list[2]))
        print(ret)

    def run(self):
        # self.create_date()
        self.str2date()


class DatetimeStr:
    def create_datetime(self):
        # datetime完整时间
        date1 = datetime(2020, 7, 3, 14, 30, 0)     # 2020-07-03 14:30:00
        hour = date1.hour       # 14
        minute = date1.minute   # 30
        second = date1.second   # 0

        # now()：类方法
        now = datetime.now()    # 2020-07-03 10:22:32.028507
        # time()：实例方法，取时间的 时-分-秒部分
        now = date1.time()      # 14:30:00

        # date只能：年-月-日
        date2 = date(2020, 7, 3)    # 2020-07-03
        print(type(date2))

        # time只能：时-分-秒
        date3 = date_time(23, 59, 59)   # 23:59:59

    def str2datetime(self, time_str):
        # %Y : 2020     年
        # %m : 01-12    月
        # %d : 0-31     日
        # %H : 0-23     时
        # %M : 00-59    分
        # %S : 00-59    秒
        # %w : 0-6      周几，0-星期天，1-星期一
        # %x : 07/03/20
        # %X : 10:30:08

        # %j : 001-365 年内的第几天

        # %% %号本身
        # time_str = "2020-07-07 14:39:18"
        ret_str = "%Y-%m-%d %X"
        ret = datetime.strptime(time_str, ret_str)
        print(ret)
        return ret

    def datetime2str(self):
        now = datetime.now()
        ret = now.strftime("%Y-%m-%d %H:%M:%S")
        print(ret)
        print(type(ret))

    def datetime2date(self):
        now_datetime = datetime.now()
        now_date = now_datetime.date()

    def pre_day(self):
        date1 = datetime(2020, 7, 3, 14, 30, 0)
        date2 = datetime(2020, 7, 1, 14, 30, 0)

        sub_time = (date2 - date1).days
        if sub_time > 0:
            print(f"{date1}为最新时间")
        elif sub_time == 0:
            print("时间相同")
        else:
            print(f"{date2}为最新时间")

    def run(self):
        # self.create_datetime()
        # self.str2datetime()
        # self.datetime2str()
        # self.time_sub()
        self.pre_day()
        pass


class Delta:
    def create_deltatime(self):
        t = datetime.now()  # 2020-07-03 11:03:55.697672
        print(t)

        # 只能是 天-时-分-秒，不能有年和月
        td = timedelta(days=0, minutes=59, seconds=59)
        print(str(td))  # 0:59:59

        days = td.days
        total_seconds = td.total_seconds()
        seconds = td.seconds

        # 加减
        ret = t + td        # 2020-07-03 12:03:54.697672

    def delta2str(self):
        t1 = datetime.now()
        time.sleep(5)
        t2 = datetime.now()
        t_sub = t2 - t1  # 0:00:05.000888

        # timedelta只有total_seconds/days/seconds属性，无法获取分钟
        # 可手动计算分钟
        total_seconds = t_sub.total_seconds()
        hour = total_seconds // 3600
        minute = (total_seconds % 3600) // 60
        second = total_seconds % 60

        t3 = datetime.now()  # 2020-07-03 10:41:45.933229
        t_add = t3 + t_sub  # 2020-07-03 10:41:50.934117
        print(t_add)

    def run(self):
        self.create_deltatime()
        # self.delta2str()


if __name__ == '__main__':
    # des = DateStr()
    # des.run()

    ds = DatetimeStr()
    ds.run()

    # d = Delta()
    # d.run()


