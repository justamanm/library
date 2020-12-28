绝对路径和相对路径

- 绝对路径：`/`开头
  - `/root/data/book.txt`
- 相对路径：
  - 相对的是工作路径(working directory )
    - 在pycharm中，默认执行文件即为工作路径
      - 直接右键执行`/data/project/main/run.py`，工作目录是run.py，os/open相对的就是run.py
    - 在命令行中，默认执行路径为当前所在命令
      - 在`/data/project`目录下执行`python main/run.py`，工作目录是project，os/open相对的是project
  - `./`或直接路径开头
    - `./data/book.txt`
    - `data/book.txt`



\__init__.py

- 在python3.2之前，模块package下必须要有\__init__.py文件
- 在python3.2之后，\__init__.py不是必要的，没有也行
- \_\_init\_\_.py中的\__call__属性可以限制可以导出的子模块、子属性
- 参考：[你常常看到的 __init__.py 到底是个啥？ - 知乎](https://zhuanlan.zhihu.com/p/130927618)





