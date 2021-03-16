# -*- coding: utf-8 -*-

import sys


def bundle_or_not():
    # 通过sys.frozen和sys._MEIPASS可以确定程序是否为打包还是脚本
    if getattr(sys, 'frozen', False) and not hasattr(sys, '_MEIPASS'):
        print('running in a PyInstaller bundle')
    else:
        print('running in a normal Python process')


def current_path():
    # 脚本执行时是python解释器位置
    # 打包执行时是exe位置
    print(sys.executable)
    
    # python后面所跟的路径 xxx/xx.py
    # 打包：xxx/xx.exe
    print(sys.argv[0])


if __name__ == '__main__':
    current_path()