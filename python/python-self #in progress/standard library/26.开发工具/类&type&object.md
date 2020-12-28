metaclass

- 创建类的类

  ```python
  
  ```

  

type&object两条线

- \_\_class\_\_用来查看type

- \__bases__用来查看继承关系

  ```python
  class type(object):
      """
      type(object_or_name, bases, dict)
      type(object) -> the object's type
      type(name, bases, dict) -> a new type
      """
      def mro(self):
          pass
      
  class object:
  ```

- 关系

  ```python
  type.__class__  <class 'type'>
  object.__class__  <class 'type'>
  
  type.__bases__  (<class 'object'>,)
  object.__bases__  ()
  ```



[`abc`](https://docs.python.org/3/library/abc.html#module-abc) — Abstract Base Classes

- [定义](https://docs.python.org/3/glossary.html#term-abstract-base-class)

> Abstract base classes complement [duck-typing](https://docs.python.org/3/glossary.html#term-duck-typing) by providing a way to define interfaces when other techniques like [`hasattr()`](https://docs.python.org/3/library/functions.html#hasattr) would be clumsy or subtly wrong (for example with [magic methods](https://docs.python.org/3/reference/datamodel.html#special-lookup)). 
>
> ABCs introduce virtual subclasses, which are classes that don’t inherit from a class but are still recognized by [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance) and [`issubclass()`](https://docs.python.org/3/library/functions.html#issubclass) .
>
> Python comes with many built-in ABCs for data structures (in the [`collections.abc`](https://docs.python.org/3/library/collections.abc.html#module-collections.abc) module), numbers (in the [`numbers`](https://docs.python.org/3/library/numbers.html#module-numbers) module), streams (in the [`io`](https://docs.python.org/3/library/io.html#module-io) module), import finders and loaders (in the [`importlib.abc`](https://docs.python.org/3/library/importlib.html#module-importlib.abc) module). You can create your own ABCs with the [`abc`](https://docs.python.org/3/library/abc.html#module-abc) module. 
>
> 当诸如hasattr（）之类的其他技术笨拙或巧妙地错误（例如，使用魔术方法）时，抽象基类通过提供一种定义接口的方式来补充鸭式输入。
>
> ABCs使得类可以实现，虽然没有继承但依然被诸如isinstance/issubclass识别为True
>
> python的很多内置数据结构模块基于/使用了ABCs，如numbers、io、collections.abc

[`collections`](https://docs.python.org/3/library/collections.html#module-collections)

- 包括一些基于ABCs的衍生类

[`collections.abc`](https://docs.python.org/3/library/collections.abc.html#module-collections.abc) 

- 用来检测类或对象是否提供了对应的接口，如实现了`__hash__`方法的是hashable对象





types-typing-collections

- typing，内置数据类型的别名

  ```python
  import typing
  
  typing.List		# List = _alias(list, 1, inst=False, name='List')
  typing.Tuple
  typing.Dict
  typing.Set
  typing.Iterator
  typing.Generator
  typing.Type
  typing.Mapping
  ```

- [`collections.abc`](https://docs.python.org/3/library/collections.abc.html?highlight=collections%20iterable#module-collections.abc) — Abstract Base Classes for Containers

  - collections.abc.Iterator/Generator与type.Iterator/Generator是同一个指向--typing.py

  <img src="pic/容器-collections.abc.png" width="80%">

  

- types

  ```python
  import types
  types.FunctionType
  types.GeneratorType
  types.CoroutineType
  types.MethodType
  types.ModuleType
  types.TracebackType
  types.FrameType
  ```

  