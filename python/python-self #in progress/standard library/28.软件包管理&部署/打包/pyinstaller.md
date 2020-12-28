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

#### 参数

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
             pathex=['D:\\python\\code\\moko\\repository\\python\\2020\\9.24-ocr\\qrcode_package_test\\qrcode_package'],
             # 添加二进制文件，如pyinstaller找不到的一些第三方模块依赖的动态库dll
             binaries=[(r"C:\Program Files\python_virtual\package\Lib\site-packages\pyzbar\libiconv.dll", "pyzbar"), (r"C:\Program Files\python_virtual\package\Lib\site-packages\pyzbar\libzbar-64.dll", "pyzbar")],
             # 列表，其中是元组，元组的内容与--add-data一致
             datas=[("modules/info":"modules/info")],
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

通过sys.exit(num)  num取[0,255]

- 参看[python脚本如何 返回值给调用它的shell？ - 大周的回答 - 知乎](https://www.zhihu.com/question/22859506/answer/22883534)
- 缺点是只能传数字，不能传字符串数据
- 使用这种方式，必须要与调用者表明数值对应的信息

通过控制台打印信息

- 需要返回具体信息时，使用此种方式



### 问题&解决

#### dll错误

如：upx异常-vcruntime140.dll

<img src="./pic/upx-vcruntime异常.png">

解决：

- [UPX breaking vcruntime140.dll (64bit) #1565](https://github.com/pyinstaller/pyinstaller/issues/1565)
- 即：加--upx-exclude参数，可重复使用以应对需要排除多个dll的情况
  - [官方参数说明](https://pyinstaller.readthedocs.io/en/stable/usage.html#general-options)



#### 有的模块无法被打包

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













