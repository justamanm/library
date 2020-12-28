- 偏函数

  - 对已有函数定制化，参数由左向右固定

  ```python
  from functools import partial
  
  def mod(n, m):
      print(n % m)
  
  mod_by_100 = partial(mod, 100)
  mod_by_100()
  ```

  