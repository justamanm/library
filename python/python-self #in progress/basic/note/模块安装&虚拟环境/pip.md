### 一般模块

用pip安装即可

#### pip常用命令

```bash
# 生成requirements.txt
pip freeze > requirements.txt

# 从requirements中安装
pip install -r requirements.txt

# 离线安装：requirements中的模块使用本地目录中的
pip3 install --no-index --find-links=./本地模块所在目录 -r requirements.txt
```







### 难装模块

#### whl文件

- 去pypi官网下载源码
- pip install [whl文件路径\whl文件]



#### setup源码安装

- 下载源码压缩包
- python setup.py build
- python setup.py install



#### 从https安装

cmd中无法从https安装，因为ssl的问题，所以最好转成http安装

如从github，将https换成http是没问题的

```bash
# requirements.txt中

# 原本用了https，无法安装
timeseriescrossvalidation @ git+https://github.com/DidierRLopes/TimeSeriesCrossValidation.git@master

# 更改成http，且使用加速地址，即可安装成功
timeseriescrossvalidation @ git+http://github.com.cnpmjs.org/DidierRLopes/TimeSeriesCrossValidation.git@master

```





### 源配置

配置文件：

- windows下位置：C:\Users\Mr.V\pip\pip.ini
- linux下位置：~/.pip

默认配置：

```bash
[global]
index-url=https://pypi.org/simple
[install]
trusted-host=pypi.org
```

国内源地址：

```bash
# 豆瓣：
http://pypi.douban.com/simple/
# 阿里云：
http://mirrors.aliyun.com/pypi/simple/
# 清华：
https://pypi.tuna.tsinghua.edu.cn/simple
# 中国科技大学 
https://pypi.mirrors.ustc.edu.cn/simple/
# 华中理工大学
http://pypi.hustunique.com/
# 山东理工大学
http://pypi.sdutlinux.org/
```

修改配置文件：

> 创建.pip文件夹
>
> mkdir ~/.pip
>
> 创建pip.conf配置文件
> vim ~/.pip/pip.conf
>
> 然后将下面这两行复制进去就好了
> [global]
> index-url = https://mirrors.aliyun.com/pypi/simple
>
> 其他地址：豆瓣：http://pypi.douban.com/simple/（注意末尾加 / ，否则无法）

 