raise：主动抛出一个异常对象（不是类），可以包含异常信息



继承：如subException继承了Exception

- 如果先捕获Exception，则不会再捕获子类异常

  ```python
  class A(Exception):
      pass
  
  class B(A):
      b = 2
      pass
  
  try:
      raise B()
  except A:		# 会进入A，而不会进入B
      print("a")
  except B:
      print("b")
  ```

- 子类异常是父类的特定实现，父类可以catch所有的子类，但子类只能catch自己的类



raise from & raise

打印内容不同，体现在except、else、finally中又出现异常时

- raise

  ```python
  try:
      raise ZeroDivisionError()
  except ZeroDivisionError:
      raise ValueError
      
  Traceback (most recent call last):
    File "D:/python/code/library/python/python-self #in progress/basic/8.异常/exception_mod.py", line 17, in <module>
      raise ZeroDivisionError()
  ZeroDivisionError
  
  During handling of the above exception, another exception occurred:
  
  Traceback (most recent call last):
    File "D:/python/code/library/python/python-self #in progress/basic/8.异常/exception_mod.py", line 19, in <module>
      raise ValueError
  ValueError
  ```
  - 处理异常时又出现另一个异常

- raise from

  ```python
  try:
      raise ZeroDivisionError()
  except ZeroDivisionError as e:
      raise ValueError from e
      
  Traceback (most recent call last):
    File "D:/python/code/library/python/python-self #in progress/basic/8.异常/exception_mod.py", line 17, in <module>
      raise ZeroDivisionError()
  ZeroDivisionError
  
  The above exception was the direct cause of the following exception:
  
  Traceback (most recent call last):
    File "D:/python/code/library/python/python-self #in progress/basic/8.异常/exception_mod.py", line 19, in <module>
      raise ValueError from e
  ValueError
  
  Process finished with exit code 1
  ```

  - 上面的异常是接下来的异常的直接原因，指明了直接关系
  - raise from三种：
    - 异常类
    - 异常对象
    - None



参考：[Python 中 raise 和 raise/from 的区别](https://blog.csdn.net/jpch89/article/details/84315444)









