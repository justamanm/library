### 概述

官方文档

- [5. The import system](https://docs.python.org/3/reference/import.html)
- [PEP420-Implicit Namespace Packages](https://www.python.org/dev/peps/pep-0420)



### import system

sys.modules

- 当前运行环境中装载的所有模块
- 是字典



命名空间

- 函数：local namespace
- 模块：global namespace
- 内置



如果import在函数内，则会导入函数的命名空间中，而不是模块命名空间



[参看](https://blog.csdn.net/weixin_38256474/article/details/81228492)



### 两种导入方式

- 导入时会执行的文件

目录

```bash
pack1
	__init__.py
	apple.py
test.py
```

`__init__.py`

```python
a = 1
print(123)
b = 2
print(234)
```

`apple.py`

```python
print(345)
a = 1
print(567)
```



导包方式一：`test.py`

```python
# 先执行__init__.py，在执行apple.py，都会执行完整个文件
import pack1.apple

# 输出
123
234
345
567
```

导包方式二：`test.py`

```python
# 与import pack1.apple一致
# 先执行__init__.py，在执行apple.py，都会执行完整个文件
from pack1 import apple

# 输出
123
234
345
567
```

即，导包时先执行`__init__.py`，再去执行要导入变量所在的文件



### 其他

#### if语句可以控制导包

```python
if use_sentry:
    # from sentry_sdk import capture_exception
    from config import config_sentry
```









