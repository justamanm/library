import os
import sys

# 执行命令，读取命令执行结果字符串
# ret = os.popen("sudo ps aux |grep supervisord | grep -v grep", "r").read()
# print(ret)

# 仅执行，获取不到执行结果字符串
# os.system("service supervisord start")

# windows下路径前要加r
path = r"D:\python\code\pool\tech_pool\python\脚本"
with open(path + "/a.txt", "w", encoding="utf8") as f:
    f.write("abc")