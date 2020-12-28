import os
import sys


def windows_add_r():
    """windows下路径前要加r"""
    path = r"D:\python\code\pool\tech_pool\python\脚本"
    with open(path + "/a.txt", "w", encoding="utf8") as f:
        f.write("abc")


def basename():
    """获取路径中的文件名（即最后'/'后面的）"""
    ret = os.path.basename(os.path.abspath(__file__))
    print(ret)


if __name__ == '__main__':
    basename()