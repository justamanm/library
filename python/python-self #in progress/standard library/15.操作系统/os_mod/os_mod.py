

def execute_command():
    """1.执行命令，读取命令执行结果字符串"""
    ret = os.popen("sudo ps aux |grep supervisord | grep -v grep", "r").read()
    print(ret)

    """2.仅执行，获取不到执行结果字符串"""
    os.system("service supervisord start")