# ��;����֤�ļ���СΪָ����С�����������׺����+1���½��ļ�����д��
# �÷�������־�����ļ��������ģ�����run��������

import os
import psutil
import re
import traceback
from flask import current_app as app


class ProcessFile:
    def __init__(self):
        # ������־Ŀ¼
        self.log_path = os.path.dirname(os.path.abspath(__file__)) + "/log"

        self.file_name = "flask_stderr.log"
        self.file_pre = self.file_name.split(".")[0]
        self.file_path = os.path.join(self.log_path, self.file_name)
        # print(self.file_path)

    def get_size(self):
        self.file_size = os.path.getsize(self.file_path) // (1024*1024)
        print(f"��־�ļ���С��{self.file_size}M")

    def rename_log(self):
        """
        �����־������������
        ��������д���ʼ����û�к�׺��С���ļ�����test.log
        ����ļ�����һ����С��������д���test.log������Ϊ��׺����+1��Ȼ�󴴽��µ�test.log����д��
        :return:
        """
        suffix_num_list = []
        status = 1

        for root, dirs, files in os.walk(self.log_path):
            # print(files)
            # ��ȡָ���ļ��ĺ�׺
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

            # ���test.log�����ڣ�����
            # �Ѵ��ڣ��������󴴽�
            if os.path.exists(self.file_path):
                # rename������bug������FileExistsError�ļ��Ѵ����쳣
                try:
                    print("��������־�ļ�")
                    os.rename(self.file_path, self.new_file)
                except Exception as e:
                    print(traceback.format_exc())
            # print(self.file_path)
            with open(self.file_path, "a+"):
                print("�����µ���־�ļ�")
            break

    def run(self):
        print("------------������־�ļ���С��10M��")
        self.get_size()
        if self.file_size >= 10:
            self.rename_log()
        print("------------�������")


if __name__ == '__main__':
    p = ProcessFile()
    p.run()