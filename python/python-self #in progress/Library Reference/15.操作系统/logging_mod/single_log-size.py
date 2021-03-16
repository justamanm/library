import argparse
import logging
import os
from datetime import datetime


# ����������
from typing import Union

parser = argparse.ArgumentParser(description="used for test")

# ��ѡ����
parser.add_argument("-debug", "-d", required=True, type=int, help="--debug")
parser.add_argument("--crop", "-c", required=True, type=str, help="--crop")
parser.add_argument("--rotate", "-r", required=True, type=int, help="--rotate")
parser.add_argument("--path", "-p", required=True, type=str, help="--path")


logger = logging.getLogger("single_log")  # ������������root logger
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "[%(asctime)s] %(levelname)s in %(filename)s[%(lineno)d]: �� %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S')

# �����ļ���С��������С���½����������д��ֱ��ָ����С
# ���壺�����������ļ��������ļ���os.listdir[-1]��ȡ�����������ļ���׺+1�����
path_pa = os.path.dirname(os.getcwd())
path_log = os.path.join(path_pa, "log/").replace("\\", "/")

if not os.path.exists(path_log):
    os.mkdir(path_log)
log_file = path_log + str(datetime.now()).split(" ")[0] + "-log.txt"

if os.listdir(path_log):
    last_log_file = path_log + os.listdir(path_log)[-1]
    size = os.path.getsize(last_log_file) // (1024*1024)
    if size < 10:
        log_file = last_log_file

# ʹ��FileHandler������ļ�
fh = logging.FileHandler(log_file, encoding="utf8")
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

# ���Handler
logger.addHandler(fh)
