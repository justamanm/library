### 概述

- 打包：python解释器 + 源码 + 依赖 + 资源文件，产生单一可执行文件或可执行文件夹



### 使用

#### 安装

```
pip3 install pyinstaller
```

#### 打包命令

```
pyinstaller 参数 file.py
```

#### 命令行参数

- 建议使用后面的spec文件配置

```
-F 生成单独的可执行文件
	生成单独可执行文件时，只要在主文件中被引入了(依赖，其他py文件)都会被打包
-D 生成一个目录（包含多个文件）来作为程序

--add-data 源地址;目标地址（linux下用冒号分隔，windows下用封号）
  几种情况：
  源地址是文件，放到打包目录的根目录：a.txt;"."
  源地址是文件，放到打包目录的指定目录(config)：a.txt;"config"（如果指定目录在本地不存在，打包时会自动创建）
  源地址是文件夹，放到打包文件对应的目录：modules/info;modules/info（源地址与目标地址一致即可）

--hidden-import 手动添加pyinstaller找不到的模块
-w --windowed, --noconsole；打包成窗口应用
-c --console, --nowindowed；默认选项，打包成控制台应用
--upx-dir=upx-3.96-win64 使用upx压缩

```

执行结束会产生build和dist两个文件夹

- build存放中间文件，可删除
- dist下即生成的可执行文件(夹)

注：在虚拟环境下打包时，必须保证环境中有pyinstaller，否则仍然使用的是默认环境



#### [upx](https://github.com/upx/upx)

[下载](https://github.com/upx/upx/releases/tag/v3.96)后解压，放到程序主目录下

使用

```
--upx-dir=upx-3.96-win64
```

一般直接使用，不需要额外参数；在-D模式下，需要用`--upx-exclude`参数排除一些动态库，见后面问题&解决

参看

- [官方参数说明](https://pyinstaller.readthedocs.io/en/stable/usage.html#general-options)





#### 建议使用spec文件打包

1.先生成打包对应的spec文件

```
pyi-makespec main.py
```

- 会在当前目录生成main.spec文件

2.配置spec



#### spec文件解析

spec文件中主要包含4个class: Analysis, PYZ, EXE和COLLECT.

- Analysis以py文件为输入，它会分析py文件的依赖模块，并生成相应的信息
- PYZ是一个.pyz的压缩包，包含程序运行需要的所有依赖
- EXE根据上面两项生成
- COLLECT生成其他部分的输出文件夹，COLLECT也可以没有

```python
# -*- mode: python ; coding: utf-8 -*-
from pyzbar import pyzbar
from pathlib import Path


block_cipher = None


a = Analysis(['main.py'],
             # Analysis在下面的文件夹中搜索依赖模块的文件，默认当前打包路径
             # 有些模块找不到时，需要指定site-packages目录
             # 注：不要用r""，可能会有x 错误
             pathex=['D:\\python\\code\\moko\\repository\\python\\2020\\9.24-ocr\\qrcode_package_test\\qrcode_package', "C:/Program Files/python_virtual/baidu/Lib/site-packages/paddleocr"],
             # 添加二进制文件，如pyinstaller找不到的一些第三方模块依赖的动态库dll
             # 除了直接指定dll文件，还可以指定文件夹，和data类似
             binaries=[(r"C:\Program Files\python_virtual\package\Lib\site-packages\pyzbar\libiconv.dll", "pyzbar"), (r"C:\Program Files\python_virtual\baidu\Lib\site-packages\paddle\libs\libiomp5md.dll", "./paddle/fluid/")],
             # 列表，其中是元组，元组的内容与--add-data一致
             datas=[("modules/info":"modules/info")],
             # pyinstaller无法自动找到的模块，但在打包后执行时报错
             # 直接写模块名称，而不是路径
             hiddenimports=["imghdr", "imgaug", "pyclipper"],
             hookspath=[],
             runtime_hooks=[],
             # pyinstaller找到的实际不需要的模块，进行排除
             excludes=["matplotlib", "pandas", "tornado"],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')

```

##### pathex

- 相当于配置环境变量
- pyinstaller默认一般可以找到最外层的模块，但经常找不到模块内部的导入
  - 原因是缺少了导包的环境变量



### windows使用

- ```pyinstaller -F manager.py --add-data modules\info;modules\info```

- 问题

  ```bash
  # 问题1：打包时提示无法导入win32com
  在打包环境中安装pywin32模块：python -m pip install pypiwin32
  
  # 问题2：打包后启动，闪退
  打包成控制台程序，然后在cmd中执行，会输出错误信息
  用录屏工具查看闪退报错信息
  
  # 问题3：No module named 'pkg_resources.py2_warn'
  解决：环境\site-packages\pkg_resources\_init_.py，注释68行：#import('pkg_resources.py2_warn')
  
  # 问题4：想启动时没有命令行窗口，但打包时不加-w参数可正常启动，加-w参数后启动报错
  解决：原因未知，打包时不加-w，以服务启动打包后exe文件
  ```





### centos6下使用

- ```pyinstaller -F manager.py --add-data modules\info;modules\info```

- 问题

  ```python
  # 问题一：pyinstaller: command not found
  # 解决：
  cp /usr/local/python3/bin/pyinstaller /usr/bin
  
  # 问题二：运行pyinstaller -F run.py
  # 提示：If you're building Python by yourself, please rebuild your Python with `--enable-shared` (or, `--enable-framework` on Darwin).
  # 尝试：yum install python-devel python-dev，复制安装目录/lib/*到/usr/lib64,都不行
  # 解决：重装python，./configuration 加参数 --enable-shared
  下载python包--》解压缩
  ./configuration --prefix=/usr/local/python36 --enable-shared 
  make && make install
  
  # 问题三：python: error while loading shared libraries: libpython3.6m.so.1.0: cannot open shared object file
  # 原因：python运行时没有加载到libpython3.6m.so.1.0 这个库文件，将其复制到相应目录，输入下列命令即可：
  cp /usr/local/python3/lib/libpython3.6m.so.1.0 /usr/lib64/
  ```





### 其他

#### 生成的exe包含什么

pyinstaller自动找到的部分依赖会编译到exe中

- 如paddleocr不会被单独打包(即打包路径下有paddleocr文件夹)，会被打包到exe中

而依赖所在的路径在spec中的pathex配置

```bash
# 1.
a = Analysis(['paddleocr_package.py'],
			# 没有写paddleocr的路径，所以打包后需要手动将文件夹复制到打包目录
             pathex=['D:\\python\\code\\moko\\repository\\python\\2020\\9.24-ocr\\deploy_demo\\paddleocr_package'],
             binaries=[])
打包目录：
main
	tools
	ppocr
	paddle
	main.exe

# 2.
a = Analysis(['paddleocr_package.py'],
			# 加上paddleocr的路径，其中需要的tools和ppocr会被打包进exe中
             pathex=['D:\\python\\code\\moko\\repository\\python\\2020\\9.24-ocr\\deploy_demo\\paddleocr_package', r"C:/Program Files/python_virtual/baidu/Lib/site-packages/paddleocr"],
             binaries=[])
             
打包目录：
main
	paddle
	main.exe # 包含了tools和ppocr
```



如paddleocr打包时：



#### 打包大小&执行速度

- 主要是一些模型占用比较大
- 打包成单一exe和文件夹的形式，大小也不一样

对比示例：

- exe文件

  ```bash
  # 不压缩：50M
  # 执行速度：3s
  pyinstaller --clean -F main.py
  
  # 压缩：33M
  # 执行速度：6s
  # 必须upx不压缩vcruntime140.dll，否则报错
  # 如果压缩ucrtbase.dll则会报错，但可以正常执行，建议不压缩
  pyinstaller --clean -F --upx-dir=upx-3.96-win64 --upx-exclude=vcruntime140.dll --upx-exclude=ucrtbase.dll main.py
  ```

- 文件夹

  ```bash
  # 不压缩：154M
  # 执行速度：0.8s
  pyinstaller --clean -D main.py
  
  # 压缩：37M
  # 执行速度：2s
  # 默认不会打包pyzbar，要在main.spec中加入hiddenimports=["pyzbar"]
  pyinstaller --clean -D --upx-dir=upx-3.96-win64 --upx-exclude=vcruntime140.dll main.py
  ```



#### 执行路径定位

参考：[pyinstaller说明](https://pyinstaller.readthedocs.io/en/stable/runtime-information.html#using-sys-executable-and-sys-argv-0)

- 在打包后，`os.path.abspath`会异常（为调用者的路径，而非打包主程序所在目录）
- 故使用`sys.argv[0]`，或使用`sys.executable`



#### 控制台输出

1.打包exe如果报错，控制台会输出异常信息，如1/0

```
Traceback (most recent call last):
  File "main.py", line 20, in <module>
  File "main.py", line 15, in test
ZeroDivisionError: division by zero
[17068] Failed to execute script main
```

2.使用argparse，未传参，也会输出异常信息

```
usage: main.exe [-h] [--crop CROP] [--resize RESIZE] path
main.exe: error: the following arguments are required: path
```



#### 返回值

如果不主动调用sys.exit()

- 0：正常结束
- 负数：程序报错导致执行失败
- 正数：exe本身错误返回正数，如路径不正确

通过sys.exit(num)  num取[0,255]

> import sys
> sys.exit(n)          // n is the value returned to shell
>
> Response to your response:
> The range of return value is [0, 255] in shell, and any number that exceeds this range will be converted as                 n%256
> Negative values are reserved for errors of program running.
>
> [python脚本如何 返回值给调用它的shell？ - 大周的回答 - 知乎](https://www.zhihu.com/question/22859506/answer/22883534)

- 缺点是只能传数字，不能传字符串数据
- 使用这种方式，必须要与调用者表明数值对应的信息

通过控制台打印信息

- 需要返回具体信息时，使用此种方式



#### 打包自定义模块

导入的自定义的模块是会被pyinstaller发现的

所以不会出现找不到的问题（暂时没遇到）



### 问题&解决

#### upx压缩-dll错误

如：upx异常-vcruntime140.dll

<img src="./pic/upx-vcruntime异常.png">

解决：

- [UPX breaking vcruntime140.dll (64bit) #1565](https://github.com/pyinstaller/pyinstaller/issues/1565)
- 即：加--upx-exclude参数，可重复使用以应对需要排除多个dll的情况
  - [官方参数说明](https://pyinstaller.readthedocs.io/en/stable/usage.html#general-options)



#### 缺失dll

（在-D文件夹模式）

原因：和pyinstaller的发现模块机制有关，只会打包直接引用的模块，而不会打包通过ctypes加载的动态库

- [参看pyinstaller官方文档](https://pyinstaller.readthedocs.io/en/latest/feature-notes.html?highlight=ctypes#ctypes-dependencies)

```
from ctypes import *
# This will pass undetected under PyInstaller detect machinery,
# because it's not a direct import.
handle = CDLL("/usr/lib/library.so")
handle.function_call()
```

- [参看：Failed to load dynlib/dll libiconv.dll](https://github.com/NaturalHistoryMuseum/pyzbar/issues/27)

解决方式一：将缺少的动态库dll按照错误信息放到生成的exe目录中即可，缺点是每次重新打包都要放重新放一次，但也是最便捷的方式

解决方式二：更改spec，将缺少的动态库手动加入

```python
binaries=[("缺少的dll路径", "模块名称")]		# 名称可由错误信息确定，一般就是模块的名称
如：binaries=[(r"C:\Program Files..\site-packages\pyzbar\libiconv.dll", "pyzbar"),]
```

- 注：如果配置无误还是不行，可删除打包cache，目录：`C:\Users\xxx\AppData\Roaming\pyinstaller`，删除其中的文件夹

（虽然方式类似，但下面的的实践不可行）

```python
# 1.修改pyzbar源码wrapper.py
EXTERNAL_DEPENDENCIES

# 2.配置spec文件
# pyzbar not detected because they are loaded by ctypes
from pathlib import Path
import pyzbar
a.binaries += TOC([
    (Path(dep._name).name, dep._name, 'BINARY')
    for dep in pyzbar.EXTERNAL_DEPENENCIES
])
```

参考：

- [关于tkinstaller打包含有pyzbar库时出现的问题](https://blog.csdn.net/Sullivan986/article/details/104831491)
  - 提出将两个缺少的dll直接放到打包目录即可
- [pyinstaller-issue：pyzbar -- ctype module not found. #3056](https://github.com/pyinstaller/pyinstaller/issues/3056)

> Thanks for your help.
>
> The module pyzbar depends on two dll files. While adding to the Analysis binaries i made a mistake.
>
> binaries = [(path,''),(path,'')] worked very well.
> With windows the cache is created in "AppData\Roaming\pyinstaller\bincache00_py27_32bit", when i was trying to rerun the .specfile it did'nt work proper so i went and removed the cache and rerun. Now it worked.

- [zbar-issue：Failed to load dynlib/dll libiconv.dll #27](https://github.com/NaturalHistoryMuseum/pyzbar/issues/27)
  - 提供一种解决思路，虽然不可行

>Freezers such as pyinstaller and cx_Freeze are not able to find libraries loaded using [ctypes](https://docs.python.org/3.6/library/ctypes.html). pyzbar exposes its binary dependencies in `EXTERNAL_DEPENDENCIES` - a list of instances of `ctypes.CDLL`. You can hack these into a pyinstaller freeze - e.g., via a [pyinstaller spec file](https://github.com/NaturalHistoryMuseum/inselect/blob/196a3ae2a0ed4e2c7cb667aaba9a6be1bcd90ca6/inselect.spec#L36).



#### paddlocr创建子进程

解决方法：[paddle-issue](https://github.com/PaddlePaddle/Paddle/issues/29660)

原因：

- 是paddlepaddle的问题，而不是paddleocr的问题
- 具体是在`site-packages/paddle/dataset/image.py`中会使用subprocess创建子进程

解决：

- 更改image.py为[这样](https://github.com/PaddlePaddle/Paddle/pull/26200/files)，加上`and not hasattr(sys, '_MEIPASS')`

  ```python
  # if six.PY3:
  if six.PY3 and not getattr(sys, 'frozen', False) and not hasattr(sys, '_MEIPASS'):
      import subprocess
      import sys
      import_cv2_proc = subprocess.Popen(
          [sys.executable, "-c", "import cv2"],
          stdout=subprocess.PIPE,
          stderr=subprocess.PIPE)
  ```

- 使用的是`getattr(sys, 'frozen', False)`

  - `sys.frozen`用来判断是python源程序还是打包后的程序

    ```python
    # 如果是打包程序则不创建子进程
    if six.PY3 and not getattr(sys, 'frozen', False):
        import subprocess
        import sys
        import_cv2_proc = subprocess.Popen(... ...)
    ```

- [pyinstaller对sys.frozen的解释](https://pyinstaller.readthedocs.io/en/stable/runtime-information.html)

  > When a bundled app starts up, the bootloader sets the `sys.frozen` attribute and stores the absolute path to the bundle folder in `sys._MEIPASS`. 
  >
  > 当一个打包程序启动时，bootloader会给sys.frozen配置值，给sys._MEIPASS设置路径信息

  - 示例：

    ```python
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        print('running in a PyInstaller bundle')
    else:
        print('running in a normal Python process')
    ```

    

另外，缺少的dll的问题

- 将缺少的dll复制到打包目录的`paddle/libs`目录下
- libs目录打包后是不存在的，需要创建，直接将原libs文件夹复制过来即可



#### 缺少模块

##### paddleocr-package案例

原代码

```python
from paddleocr import PaddleOCR

# 在__init__.py中
from .paddleocr import PaddleOCR
from .tools.infer.utility import draw_ocr

# 在paddleocr.py中
from tools.infer import predict_system
from ppocr.utils.utility import initial_logger
```

报错：import paddleocr语句报错，提示：paddleocr\paddleocr.py中No module named 'tools'

解决：通过配置spec中的pathex来完成

```bash
pathex=[
	'D:\\python\\code\\moko\\repository\\python\\2020\\9.24-ocr\\deploy_demo\\paddleocr_package',
	r"C:\Program Files\python_virtual\baidu\Lib\site-packages"
],
```

- 还是会报错，即配置的pathex不正确，是缺少paddleocr\目录的环境变量导致

- 在代码中加入环境变量，或在pathex中配置site-packages\paddleocr可解决

  ```bash
  pathex=[
  	'D:\\python\\code\\moko\\repository\\python\\2020\\9.24-ocr\\deploy_demo\\paddleocr_package',
  	r"C:\Program Files\python_virtual\baidu\Lib\site-packages\paddleocr"
  ],
  ```



另：WindowsPath异常在配置环境变量后正常

```bash
Traceback (most recent call last):
  File "paddleocr_package.py", line 75, in <module>
  File "paddleocr_package.py", line 55, in run
  File "paddleocr.py", line 221, in __init__
  File "tools\infer\predict_system.py", line 42, in __init__
  File "tools\infer\predict_rec.py", line 61, in __init__
  File "ppocr\utils\character.py", line 46, in __init__
TypeError: expected str, bytes or os.PathLike object, not WindowsPath
```



##### paddle-flask案例

- 与paddleocr-package原因一样
- 解决方法也一致，在导包前先加入site-packages\paddleocr的环境变量



---------------------未使用-------------------------

- 项目(多个文件)打包

  - 多个源文件 + 资源文件

  - 需要修改spec文件

  - spec文件生成 

    - windows下，使用```pyi-makespec -w xxx.py ```生成
    - linux下，无法使用```pyi-makespec```命令，但在打包后会自动生成

  - spec文件类似与py文件，其中有4个类: Analysis, PYZ, EXE和COLLECT，通过传参更改配置

    - Analysis：以py文件为输入，它会分析py文件的依赖模块，并生成相应的信息
    - PYZ：是一个.pyz的压缩包，包含程序运行需要的所有依赖
    - EXE：根据上面两项生成
    - COLLECT：生成其他部分的输出文件夹，COLLECT也可以没有

    ```python
    # -*- mode: python ; coding: utf-8 -*-
    
    block_cipher = None
    
    a = Analysis(['run.py'],
                 pathex=['/home/python/estateQuery/estate_query_nolog'],
                 binaries=[],
                 datas=[],
                 hiddenimports=[],
                 hookspath=[],
                 runtime_hooks=[],
                 excludes=[],
                 win_no_prefer_redirects=False,
                 win_private_assemblies=False,
                 cipher=block_cipher,
                 noarchive=False)
    pyz = PYZ(a.pure, a.zipped_data,
                 cipher=block_cipher)
    exe = EXE(pyz,
              a.scripts,
              a.binaries,
              a.zipfiles,
              a.datas,
              [],
              name='run',
              debug=False,
              bootloader_ignore_signals=False,
              strip=False,
              upx=True,
              upx_exclude=[],
              runtime_tmpdir=None,
              console=True )
    
    ```

    



---------------------扩展----------------

- 将标准解释器替换为python-embeded版本













