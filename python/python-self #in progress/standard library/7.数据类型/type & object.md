顶端：type和object



type-类型

- 基本上内置类型的类型都是type
- type的类型是自己
- 自定义类的类型也是type
- 对象类型是其所属类



通过魔法方法`__class__`查看：

```python
class Test:
    pass
t = Test()

list.__class__  > type
Test.__class__  > type
type.__class__  > type
t.__class__  > Test
```



object-父类

- object的父类为空
- type的父类为object
- 类的父类为object
- 对象没有父类，只有类型

通过魔法方法`__bases__`查看：

```python
class Test:
    pass
t = Test()

list.__bases__  > object
Test.__bases__  > object
type.__bases__  > object
t.__bases__  > 报错
```

