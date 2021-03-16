魔法方法

```python
new、init
str、repr
del
attr、item(get,set)（不是对应方法，而是对应操作符，dog.name，poke[value]，赋值）
call
iter、next
enter、exit
dir
hash
len
eq、gt、lt、ge、le(不是对应方法，而是对应操作符，== > < >= <=)
```

- 参考：[1](https://www.cnblogs.com/hz2lxt/p/13219223.html)

魔法属性

```python
dict、slots(字典类型)
doc
class、bases
```

其他

- dir()与\_\_dict\_\_基本类似，有些对象没有dict，dir()更完整，dict是dir()的子集



open

- 如果传的是文件名，相当于是相对路径，相对的是工作目录，`os.getcwd()`
- 如果是在子模块中直接传文件名，如创建文件，则文件会被创建到主程序所在目录(工作目录)下



内置方法

```python
isinstance()
issubclass()

hasattr()
```





解释器执行相关

- 函数：会检查执行关键字参数，但不会检查和执行函数内部

  ```python
  # 前面没有定义d
  def test(a=d):	# 这里会报错
      print(d)	# 这里不会报错
  ```

- a

  ```python
  test.__class__  <class 'function'>
  
  ```

  



并发：

进程/线程

协程/异步



继承/mro















