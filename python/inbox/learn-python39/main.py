# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2021/3/3 10:46
# @Author  : Mr.V
# @FileName: main.py
# @Software: PyCharm
"""
# 类型注释


from typing import Union, Text, List, Tuple, Dict, Set, Optional


a = list[float]
print(a)

lucky_number = 42      # Safe
lucky_number * 2       # This works
a = lucky_number << 5      # Fails
print(a)