# 安装

## linux



### centos

#### centos6



#### centos7



### ubuntu

概述

- ubuntu16.04默认：安装了python2.7和python3.5
- Ubuntu18.04默认：只有python3.6.8

安装

- 安装python3.6，并更改优先级，使得输入python/python3时，启动python3.6
- 命令：`apt-get install python3.6`
- 安装完成后在`/usr/bin`查看

多个python3版本，如3.6、3.7、3.8共存

- 用conda解决即可

- 或者麻烦一些，更改优先级，使得输入python3是指定的版本

  ```bash
  # 调整Python3的优先级，使得3.6优先级较高(数字大的优先级高)：
  sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
  sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2
  
  # 更改默认值，python默认为Python2，现在修改为Python3
  sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 100
  sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 150
  ```

pip使用

- pip为python2
- pip3为python3



 ## windows

下载安装包安装即可

安装完后配置一下环境变量









![img](https://common.cnblogs.com/editor/tiny_mce/themes/advanced/img/trans.gif)