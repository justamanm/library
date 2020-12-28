# 用途：保证文件大小为指定大小，超出后将其后缀数字+1，新建文件进行写入
# 用法，在日志配置文件中引入此模块调用run方法即可

import os
import psutil
import re
import traceback
from flask import current_app as app


class ProcessFile:
    def __init__(self):
        # 配置日志目录
        self.log_path = os.path.dirname(os.path.abspath(__file__)) + "/log"

        self.file_name = "flask_stderr.log"
        self.file_pre = self.file_name.split(".")[0]
        self.file_path = os.path.join(self.log_path, self.file_name)
        # print(self.file_path)

    def get_size(self):
        self.file_size = os.path.getsize(self.file_path) // (1024*1024)
        print(f"日志文件大小：{self.file_size}M")

    def rename_log(self):
        """
        针对日志的重命名方法
        保持正在写入的始终是没有后缀大小的文件，如test.log
        如果文件超出一定大小，将现在写入的test.log重命名为后缀数字+1，然后创建新的test.log进行写入
        :return:
        """
        suffix_num_list = []
        status = 1

        for root, dirs, files in os.walk(self.log_path):
            # print(files)
            # 获取指定文件的后缀
            for f in files:
                ret = re.match(self.file_pre + ".?(\..*)", f)
                # print(ret)
                if ret:
                    if status:
                        self.file_suffix = ret.group(1)
                        status = 0

                    pre_num = f.split(".")[0].strip(self.file_pre)
                    # print(suffix_num)
                    if not pre_num:
                        pre_num = 0
                    suffix_num_list.append(int(pre_num))
            # print(suffix_num_list)
            if files and suffix_num_list:
                max_suffix = max(suffix_num_list)
                new_file = self.file_pre + str(max_suffix + 1) + self.file_suffix
                self.new_file = os.path.join(self.log_path, new_file)
                # print(self.new_file)

            # 如果test.log不存在，创建
            # 已存在，重命名后创建
            if os.path.exists(self.file_path):
                # rename方法有bug，会抛FileExistsError文件已存在异常
                try:
                    print("重命名日志文件")
                    os.rename(self.file_path, self.new_file)
                except Exception as e:
                    print(traceback.format_exc())
            # print(self.file_path)
            with open(self.file_path, "a+"):
                print("创建新的日志文件")
            break

    def run(self):
        print("------------配置日志文件大小（10M）")
        self.get_size()
        if self.file_size >= 10:
            self.rename_log()
        print("------------配置完成")


if __name__ == '__main__':
    p = ProcessFile()
    p.run()