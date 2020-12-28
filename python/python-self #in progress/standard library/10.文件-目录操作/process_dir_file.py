import os
import re
import time
import psutil


class File:
    def __init__(self):
        self.file_pre = "test"
        self.file_name = "test.txt"

    def create_file(self, file):
        # window下不支持，只支持linux
        # os.mknod("test.txt")

        # 只能使用open创建
        with open(file, "w"):
            pass

        # 创建单级目录
        # os.mkdirs("./test/a")

        # 创建多级目录
        # os.makedirs("./test/a")

    def dir_all_file(self):
        # 列出指定目录下的所有文件和文件夹
        ret = os.listdir(".")
        print(ret)

        # os.walk返回生成器
        # 分开返回指定目录下的文件列表，和文件夹列表
        # 会迭代循环所有文件及其子目录下的文件，第一次指定目录，第二次指定目录下的第一个文件夹，以此类推
        for root, dirs, files in os.walk("."):
            print("------------")

            print("所有文件")
            for f in files:
                print(f)
            break   # 如果只想获取指定目录下的文件

            print("所有文件夹")
            for d in dirs:
                print(d)

    def get_size(self):
        self.size = os.path.getsize(self.file) // (1024*1024)
        print(self.size)

    def rename(self):
        os.rename("a.txt", "a1.txt")

    def rename_log(self):
        """
        针对日志的重命名方法
        保持正在写入的始终是没有后缀大小的文件，如test.log
        如果文件超出一定大小，将现在写入的test.log重命名为后缀数字+1，然后创建新的test.log进行写入
        :return:
        """
        suffix_num_list = []
        status = 1

        for root, dirs, files in os.walk("."):
            # 获取指定文件的后缀
            for f in files:
                ret = re.match(self.file_pre + ".?(\..*)", f)
                if ret:
                    if status:
                        self.file_suffix = ret.group(1)
                        self.file_name = self.file_pre + self.file_suffix
                        status = 0

                    pre_num = f.split(".")[0].strip(self.file_pre)
                    # print(suffix_num)
                    if not pre_num:
                        pre_num = 0
                    suffix_num_list.append(int(pre_num))

            if files:
                max_suffix = max(suffix_num_list)
                self.new_file = self.file_pre + str(max_suffix + 1) + self.file_suffix
                print(self.new_file)

            # 如果test.log不存在，创建
            # 已存在，重命名后创建
            if os.path.exists(self.file_name):
                # rename方法有bug，会抛FileExistsError文件已存在异常
                try:
                    os.rename(self.file_name, self.new_file)
                except:
                    pass
            self.create_file(self.file_name)

    # 查看文件被哪个进程占用着
    def open_file_pro(self):
        file_name = r"D:\python\code\moko\repository\python\2020\6.5 weixin_article\spider\flask_app\log\flask_stderr1.log"
        for proc in psutil.process_iter():
            try:
                # this returns the list of opened files by the current process
                flist = proc.open_files()
                if flist:
                    for nt in flist:
                        if nt.path == file_name:
                            print(proc.pid, proc.name)
            except Exception as e:
                # print(traceback.format_exc())
                pass

    def run(self):
        self.rename_log()

        # self.create_file()
        # self.dir_all_file()
        # self.get_size()


if __name__ == '__main__':
    f = File()
    f.run()