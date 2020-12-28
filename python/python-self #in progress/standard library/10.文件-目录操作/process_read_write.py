# TODO 注：
# f.tell()，当前指针位置，读写均会改变位置
# f.seek(offset,whence=0)，调整指针
# offset：偏移多少
# whence：参照点，0-文首，1-当前位置，2-文末

# 打开后清空内容：f.truncate()


# 读写，文件不存在创建
def w_plus():
    with open("../../python基础/test.txt", "w+") as f:
        print(f.tell())  # 刚打开时指针位置在文首，所以在后面写的时候要调整到文末
        f.write("abc")
        print(f.tell())  # 3
        data = f.read()  # 由于指针在末尾，所以读不出内容
        print(data)
        print(f.tell())  # 3


# 读写，不存在报错
def r_plus():
    with open("../../python基础/test.txt", "r+") as f:
        print(f.tell())  # 刚打开指针位置在文首
        data = f.read()
        print(data)
        f.seek(0, 2)
        f.write("\n123")


def a_plus():
    with open("../../python基础/test.txt", "a+") as f:
        print(f.tell())  # 刚打开指针位置在文末
        # f.write("xyz")
        f.seek(0, 0)    # 移动到文首
        print(f.tell())
        data = f.read()  # 读的时候指针会移动
        print(data)
        print(f.tell())  # 读完后指针这时在文末


def goto_line():
    import linecache
    data = linecache.getline("../../python基础/test.txt", 5)
    print(data)


if __name__ == '__main__':
    # a_plus()
    goto_line()