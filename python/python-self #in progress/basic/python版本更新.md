### python3.0

- 2008年12月3日 



### python3.6

- 新增`f-string`
- 许在数字中使用下划线，以提高多位数字的可读性
  - a = 1_000_000_000_000_000    # 1000000000000000 
- Windows上的 filesystem 和 console 默认编码改为UTF-8
- 



### python3.7

- Python 3.7 于 2018 年 6 月 27 日发布 
- 新增异步关键字：async-await
- dict在插入时保持顺序
- 新增[contextvar模块](https://docs.python.org/3/library/contextvars.html#module-contextvars)



### python3.8

- 赋值表达式

  ```python
  if (n := len(a)) > 10:
      print(a)
  ```

- `/`用来限制函数位置参数

  ```python
  # a和 b 只能是位置参数，c 和 d 可以是位置形参或关键字形参，而 e 或 f 要求为关键字
  def f(a, b, /, c, d, *, e, f):
      print(a, b, c, d, e, f)
  
  f(10, 20, c=30, d=40, e=50, f=60)
  ```

- `f-string`支持`f'{expr=}' `

  ```python
  user = 'eric_idle'
  member_since = date(1975, 7, 31)
  f'{user=} {member_since=}'
  "user='eric_idle' member_since=datetime.date(1975, 7, 31)"
  ```

  

### python3.9

<img src="https://justaman-1300954182.cos.ap-shanghai.myqcloud.com/library/python/official/basic/python3.9%E5%8F%98%E5%8C%96.jpeg">













