### 概述

与virtualenv区别：可以指定虚拟环境的默认目录



### 安装

```
pip3 install virtualenvwrapper
```

### 使用

```bash
# 创建python虚拟环境
mkvirtualenv [虚拟环境名称]

# 进入虚拟环境
workon [虚拟环境名称]

# 退出虚拟环境
deactivate

# 删除虚拟环境
rmvirtualenv [虚拟环境名称]

# 重命名虚拟环境
# 方法一：
pip freeze -> requirements.txt
pip install -r requirements.txt

# 方法二：（暂不用不了，提示没有cpvirtualenv命令）
# 先复制一份
cpvirtualenv [旧的虚拟环境名称] [新的虚拟环境名称]
# 在删除原来的
rmvirtualenv [旧的虚拟环境名称]

# 不要重命名，会出现不可预知的错误
```





linux下配置

```bash
上述工具装好后找不到mkvirtualenv命令，需要执行以下环境变量设置。
1.创建目录用来存放虚拟环境
     mkdir $HOME/python/python_virtual
2.在~/.bashrc中添加行：
     export WORKON_HOME=$HOME/python/python_virtual
     source ~/.local/bin/virtualenvwrapper.sh

注：virtualenvwrapper.sh也可能在/usr/local/bin下：
     source /usr/local/bin/virtualenvwrapper.sh

     如果出现No module named virtualenvwrapper … in path …或 virtualenvwrapper could not find virtualenv in your path，则再增加这两行：
     export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
     export VIRTUALENVWRAPPER_VIRTUALENV=/home/justaman/.local/bin/virtualenv
   （export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv）

3.运行使生效:
     source ~/.bashrc

参考：https://blog.csdn.net/gzy686/article/details/81811288

虚拟环境用的哪个python版本与设置的优先级有关，使用优先级高的

----update200323
pip3 install virtualenvwrapper
如果出现Command "python setup.py egg_info" failed with error code 1
则：pip3 install setuptools==33.1.1，再安装即可
```

-blog