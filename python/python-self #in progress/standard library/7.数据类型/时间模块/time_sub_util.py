from datetime import datetime


def str2datetime(time_str):
    ret_str = "%Y-%m-%d %X"
    ret = datetime.strptime(time_str, ret_str)
    return ret


def time_sub(start, end):
    # time_str1 = "2020-07-07 14:54:12"
    # time_str2 = "2020-07-07 14:54:53"
    if isinstance(start, str):
        start = str2datetime(start.split(".")[0])   # 处理2020-07-09 14:12:19.453411
    if isinstance(end, str):
        end = str2datetime(end.split(".")[0])

    t_sub = end - start
    total_seconds = t_sub.total_seconds()
    minute = int((total_seconds % 3600) // 60)
    second = int(total_seconds % 60)
    print(f"{minute}分{second}秒")