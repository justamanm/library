import subprocess
import os
import re


def get_video_bitrate(path):
    """
    获取视频的 时长 长 宽
    :param path: 视频路径
    :return:
    """
    print("begin" + "-"*50)
    process = subprocess.Popen(['ffmpeg', '-i', path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = process.communicate()
    # print(stdout.decode('utf-8'))
    pattern_bitrate = re.compile("(\d+)\s*kb\/s")
    matches = re.findall(pattern_bitrate, stdout.decode('utf-8'))
    return matches


def do_it():
    # path = os.path.dirname(os.path.abspath(__file__)) + "/1.mp4"
    path = r"D:\test_video.mp4"
    print(path)
    print('*'*50)
    ret = get_video_bitrate(path)
    print(ret)
    video_bitrate = int(ret[1])
    audio_bitrate = int(ret[-1])
    filesize = os.path.getsize(path)
    # 最终视频大小
    final_size = 24000000
    compress_bitrate = final_size*(video_bitrate + audio_bitrate)/filesize - audio_bitrate
    print('小丸工具箱 2Pass 压缩的比特率为：' + str(int(compress_bitrate)))


if __name__ == '__main__':
    do_it()