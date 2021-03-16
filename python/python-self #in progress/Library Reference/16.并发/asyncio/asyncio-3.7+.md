## [asyncio模块](https://docs.python.org/3.6/library/asyncio.html )

- 参考：

  - [Python黑魔法 --- 异步IO（ asyncio） 协程](https://www.jianshu.com/p/b5e347b3a17c )，jie'ch
  - [asyncio并发编程](https://www.jianshu.com/p/27f214de1ae2)

  

### 概述

- 异步的概念：
  - 与同步对应，解决的是堵塞在一个任务上的问题
  - 多线程、多进程、跳过+回调+eventloop（IO多路复用）都是实现的异步的不同方案

- asyncio采用的是```跳过+回调+eventloop```方式

- 只是针对多个协程间的并行，嵌套协程属于一个协程；（即协程内部的await coroutine不会加入到eventloop中）
- eventloop基于I/O多路复用



### 事件循环（eventloop）

- 程序开启一个无限的循环，程序员会把一些函数注册到事件循环上。当满足事件发生的时候，调用相应的协程函数 

- 创建：asyncio.get_event_loop()

- 方法：
  - stop()：停止事件循环

- asyncio提供两种eventloop

  - [`SelectorEventLoop`](https://docs.python.org/3.6/library/asyncio-eventloops.html#asyncio.SelectorEventLoop) ：基于[`selectors`](https://docs.python.org/3.6/library/selectors.html#module-selectors) 模块（High-level I/O multiplexing）

  - [`ProactorEventLoop`](https://docs.python.org/3.6/library/asyncio-eventloops.html#asyncio.ProactorEventLoop) ：`asyncio.ProactorEventLoop`类，仅适用于windows系统



### 协程（[coroutine](https://docs.python.org/3.6/library/asyncio-task.html)）

- 协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。协程对象需要注册到事件循环，由事件循环调用。

- 协程对象不能直接运行，在注册事件循环的时候，其实是run_until_complete方法将(coroutine)包装成为了一个任务（task）对象 

- 新旧两种声明方式：

  ```python
  # 1.使用以前的装饰器方式声明协程
  @asyncio.coroutine
  def func1():
      yield from asyncio.sleep(3)
  # func1()类型为generator，但不影响使用
  print(type(func1()))
  
  # 2.使用现在的async/await方式声明协程
  async def func2():
      for i in range(1, 11):
          print(i)
          await func1()
  # func2()类型为coroutine
  print(type(func2()))
  ```

- 执行： 

  - 单个协程：`loop.run_until_complete()`
  - 多个协程：`loop.run_until_complete(asyncio.wait(task_list))`

  ```python
  import asyncio
  
  async def hello_world():
      print("Hello World!")
  
  # 仅返回协程对象，不执行
  coroutine1 = hello_world()
  loop = asyncio.get_event_loop()
  # block call，堵塞
  # Blocking call which returns when the hello_world() coroutine is done
  # 即run_until_complete方法是堵塞的
  loop.run_until_complete(coroutine1)
  loop.close()
  ```

- 协程嵌套

  ```python
  import asyncio
  
  async def compute(x, y):
      print("Compute %s + %s ..." % (x, y))
      await asyncio.sleep(1.0)
      return x + y
  
  async def print_sum(x, y):
      result = await compute(x, y)
      print("%s + %s = %s" % (x, y, result))
  
  loop = asyncio.get_event_loop()
  loop.run_until_complete(print_sum(1, 2))
  loop.close()
  ```

  - 图解：

  <img src="./协程嵌套.png" width="90%">



### await

- 挂起当前协程，切换到下一个协程

- 挂起：future对象、协程对象

  ```python
  # 挂起future对象，直到被完成或抛出异常
  result = await future
  # 挂起协程，等待此协程的返回；协程表达式(await coroutine)必须是对另外一个协程的调用
  result = await coroutine
  
  # GatheringFuture
  restult = await asyncio.gather(*tasks)
  ```
  




### 任务（Task）

- 一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含任务的各种状态。

- 是Future的子类

- 创建任务：

  - ```asyncio.ensure_future(coroutine)```
  - ```loop.create_task(coroutine)``` 

- 执行结果：

  - task.result()，即为协程返回的数据

- 四种状态：Pending Running Done Cancelled 

  - 创建future的时候，task为pending，事件循环调用执行的时候当然就是running，调用完毕自然就是done，如果需要停止事件循环，就需要先把task取消 

  - 手动停止：task.cancel()

    ```python
    for task in asyncio.Task.all_tasks():
            print(task.cancel())	# 返回True表示cannel成功
    ```

    

  

### Future

- 代表将来执行或没有执行的任务的结果。它和Task上没有本质的区别
- Task是Future的子类





### 绑定回调

- task.add_done_callback(callback方法)

  ```python
  # 回调的最后一个参数是future对象，创建的task和这里的future对象，实际上是同一个对象(id一致)
  def callback(i, future):
      print('Callback: ', future.result())
  
  coroutine = do_some_work(2)
  loop = asyncio.get_event_loop()
  task = asyncio.ensure_future(coroutine)
  # 给task绑定回调方法
  task.add_done_callback(callback)
  loop.run_until_complete(task)
  ```





### 不同线程的事件循环

- 主线程中创建一个new_loop，然后在另外的子线程中开启一个无限事件循环。主线程通过run_coroutine_threadsafe新注册协程对象。这样就能在子线程中进行事件循环的并发操作，同时主线程又不会被block

- asyncio.run_coroutine_threadsafe(coroutine, eventloop)

  



### 方法

- loop.run_until_complete(future)
  - 参数：Future对象（task是Future的子类 ），下面两个返回Future对象
    - asyncio.wait(tasks) 
      - Returns two sets of Future: (done, pending).
      - 当传入一个协程，其内部会自动封装成task
    - asyncio.gather(*tasks)
      - Return a future aggregating results from the given coroutines or futures.
      - 当传入一个协程，会被封装成Future
- asyncio.gather(**coros_or_futures*)
  - 参数：协程或future
  - 返回：协程/future的执行结果，为GatheringFuture对象，是future的子类
  - 使用：
    - 启动事件循环：asyncio.get_event_loop(asyncio.gather(**coros_or_futures*))
    - 协程嵌套：result  = await asyncio.gather(**coros_or_futures*)
- asyncio.wait(futures)
  - 参数：task列表
  - 返回：done集合、pending集合
  - 使用：
    - 启动事件循环：asyncio.get_event_loop(asyncio.wait(futures))
    - 协程嵌套：done, pending = await asyncio.wait(futures)
- asyncio.run_coroutine_threadsafe(coroutine, eventloop)





## new

---

### asyncio源码

await的任务执行io情况的监听，有selector实现（io多路复用）

```python
base_events.py
def _run_once(self):
    # Run one full iteration of the event loop.
	event_list = self._selector.select(timeout)
```



task在源码中体现的不是很多，暴露出task的概念，结合future对象和事件循环

future是一个low-level的awaitable对象，一般不会手动创建



#### 例子

```python
import asyncio
import time

async def say_after(delay, what):
    print(delay)
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(say_after(1, "task1"))
    task2 = asyncio.create_task(say_after(2, "task2"))

    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")

# 异步执行
asyncio.run(main())
```



#### 执行步骤讲解

```python
1.创建main()的Task(Future)对象
	将future.step方法加入EventLoop.ready列表中
	if main()的状态不是pending（main中没有异步操作）:
        将结束main()函数的callback加入到event_loop的ready列表中
    else : # 会进到这里
        将结束main()函数的callback放到future(main())._callbacks列表中
    此时：event_loop.ready = [Handle(Future(main()).step())]
2.开始遍历event_loop的ready列表（会pop），执行各回调方法
	调用仅有的Future(main())的step方法
    	将step对应的future-task放入current_tasks字典中，{"loop1":Task(main())}
        result = Future(main()).send(None)	# 预激活main()
        	会将task1放入ready列表中，[Handle(Future(say_after(1, "task1")).step())]；
            会将task2放入ready列表中，[Handle(Future(say_after(2, "task2")).step())]；
            result = main()中会返回第一个await的异步任务task1
        if task1._asyncio_future_blocking is True:
            task1._asyncio_future_blocking is False
            task1.callbacks.append(self.__wakeup)
        _leave_task()，从_current_tasks中删除当前loop:main()，即切换任务
3.此时event_loop的ready列表：[Handle(Future(say_after(1, "task1")).step())，Handle(Future(say_after(2, "task2")).step())]
	分别迭代两个Future(say_after).step()：
    1.Future(say_after1).step()
    	send(None)：调用iter(asyncio.sleep())，sleep()方法中会注册回调函数
```



#### 主要的组件：事件循环&Future

```python
class EventLoop:
    self._ready = collections.deque()
    
    self._scheduled = []
    
    def call_soon():
        handle = Handle(callback)
        self._ready.append(handle)
        
    def call_later():
        # 配合asyncio.sleep()
        
    
class Future:
    self._loop = loop
    self._callbacks = []	# 一个future可能有多个callback
    
    def done(self):
        return self._state != "_PENDING"
    
    def add_done_callback():
        self._callbacks.append()
    
    # 相当于__iter__，当await task1，会调用task1的__await__()方法，返回一个Iterate
    def __await__():
        if not self.done():
            self._asyncio_future_blocking = True
            yield self
            
class Task(futures.Future):
    def __init__():
        self._loop.call_soon(self.__step, context=self._context)
    
    def __step():
    	_enter_task(self._loop, self)
        result = coro.send(None)
        blocking = getattr(result, '_asyncio_future_blocking', None)	# True
        if blocking:
            result._asyncio_future_blocking = False
            result.add_done_callback(self.__wakeup, context=self._context)
        _leave_task(self._loop, self)
        self = None
```



其他变量

```python
_current_tasks: 维护了各个event_loop正在执行的任务
    {"loop1":task, "loop2":task} 
```



#### 案例-源码解读

```python
async def corotine():
    print("start")
	await sleep("task1")
    print("end")

async def main():
    print("start")
    s1 = corotine("task1")
    s2 = corotine("task2")
    
    await s1
    await s2
    
asyncio.run(main())
```



##### 前置

放入event-loop中的都是将coroutine封装的Handle对象，且指定循环时所要执行的方法handle._callback

- 普通的协程，handle._callback是其对应的task对象的__step方法
- sleep，是_set_result_unless_cancelled方法

每个协程的Future对象的_callbacks列表属性中都会添加self.\_wakeup回调（这里的self指当前协程），用于解阻塞



##### 执行过程

1.最外层main()通过run()将自己加入到event-loop中，开始第一次循环

- 将自己pop出Handle(main().\__step)，调用其__step方法
  - 调用send()
    - 创建s1和s2，并加入到event-loop中
  - send()返回s1
  - 给s1的callback列表添加main().__wakeup回调
- 结束循环

2.开始第二次循环，此时event-loop为[s1, s2]

- pop出Handle(s1.\__step)对象，调用其__step方法
  - 调用send()
    - 创建sleep协程，给Handle(sleep)对象的\_callback添加_set_result_unless_cancelled
  - send()返回Future(sleep)
  - 给Future(sleep)的callback列表添加s1.__wakeup回调

- pop出s2，类似s1
- 结束循环

3.由于有sleep协程，在开始循环前，会先睡指定的秒数，并将Handle(_set_result_unless_cancelled)加入event-loop中

然后开始第三次循环，此时event-loop为[sleep]

- pop出Handle(sleep._set_result_unless_cancelled)，调用\_set_result_unless_cancelled
  - 将Handle(s1._wakeup)加入event-loop
- 结束循环

4.开始第四次循环，此时event-loop为[Handle(s1._wakeup)，Handle(s2.\_wakeup)]

- 其中调用s1.__step
  - s1.send()，使得在sleep处解阻塞，继续执行s1直到完成，抛出StopIteration
  - 在try StopIteration中会将s1._callbacks中的main().\_wakeup加入event-loop中
- 调用s2.__step，类似s1

5.main()._wakeup调用main().\_step()

6.调用main().__wakeup，结束main()



执行过程-进阶

应该以event-loop去理解执行过程，而不是所写的逻辑

- 1.main()被加入loop，第一次循环
  - result = task1，task1._callback绑定main().\_wakeup
  - task1和task2加入到loop，此时loop为[task1, task2]
- 2.第二次循环，执行task1和task2
  - result = sleep1/sleep2，sleep1和sleep2的_callback绑定task1/task2.\_wakeup
  - sleep1和sleep2没有加入到loop，此时loop为[]
- 3.第三次循环，循环前先实际的sleep，且将Handle(s1.\_set_result_unless_cancelled)加入到loop中
  - s1._wakeup加入到loop中
- 4.第四次循环，此时loop为[s1._wakeup]
  - s1抛StopIteration，将main()._wakeup加入到loop
- 5.第五次循环，[main._wakeup]
  - result = task2，task2._callback绑定main().\_wakeup
- 6.后面的task2的步骤和task1一样，执行3/4/5，最后main()结束



注：

- 异步并不是靠后台执行任务，执行完成后通知主程序
- 耗时任务也是在run_once主循环中执行的，起码sleep是这样的



main()及其wrapper

```python
async def main():
    task = asyncio.create_task(say_after(1, "task1"))
    await task1
    
asyncio.run(main())
```

- 如果没有被asyncio.run的wrap和await，main会顺序执行
- 如果有，main会被asyncio.run接管，await会使得main变成生成器



总结：

- 父协程调用子协程，子协程堵塞任务加入到event-loop执行，且指定循环时执行的函数
- 执行完后父协程恢复子协程运行



参考：

- [asyncio源码-案例](https://lotabout.me/2017/understand-python-asyncio/)
- [asyncio源码：复现](https://zhuanlan.zhihu.com/p/64991670)



### 第三方协程封装

#### 官方sleep封装参考

asyncio.sleep源码关键部分

```python
1.Future(sleep()) = say_after.send(None)
def sleep():
    2.future._loop.call_later(delay,futures._set_result_unless_cancelled,future, result)

_loop.call_at()  
    2.1.heapq.heappush(self._scheduled, timer)
    即：self._scheduled = [TimerHandle(when, callback, args, self, context)]
    		callback = futures._set_result_unless_cancelled
            self = event_loop
            args = future(之后其_callbacks加入了__wakeup)
            
                
3.Future(sleep()).add_done_callback(
                            self.__wakeup, context=self._context) 
	Future(sleep())._callbacks.append((__wakeup, context))

for loop.ready:
    TimerHandle(when, _set_result_unless_cancelled, args, self, context)
    run()方法执行：_set_result_unless_cancelled(Future(_callbacks[__wakeup]))
    	fut.set_result(result)
        	self._result = result
        	self._state = _FINISHED
        	self.__schedule_callbacks()
            	self._loop.call_soon(__wakeup)
                
__wakeup
	self.__step() # 这里的self是调用sleep的协程，即say_after
    	step内会say_after.send(None)，使得sleep解阻塞，say_after继续向下执行，直到结束
```



官方还封装了基本的打开文件io、网络io协程

见base_subprocess.py

- BaseSubprocessTransport
- WriteSubprocessPipeProto
- ReadSubprocessPipeProto

**第三方的协程封装类似官方的即可**



Task & Future & Handle

- Future是对coroutine的wrap

- Task是Future的封装，Task继承Future

  - asyncio.create_task返回的是Task对象
  - asyncio.sleep返回的是Future对象

- Handle

  - 是对Task/Future的callback的封装
  - event-loop中放的是Handle
    - 每个handle都绑定一个callback，是循环时实际执行的函数
      - 用asyncio.create_task创建的任务的callback都是_step()
      - asyncio.sleep的callback是_set_result_unless_cancelled

- Task/Future & Handle

  - Task/Future将自己的callback对应的Handle对象加入到循环中

    ```python
    1.Task/Future.add_done_callback()
    2.loop.call_soon()
    3.handle = events.Handle(callback,task/future,loop,context)
      _ready.append(handle)
    ```

    

  





### aysncio模拟：从yield到asyncio

异步

- 解决多任务(concurrency)而cpu空闲的问题，即最大化利用资源解决任务（i/o密集型）
- 多任务的并发，即多任务的不断切换至最终完成任务
- 对任务(协程-coroutine)的要求为：
  - 可以中断某一任务，且保留上下文
  - 恢复时接着之前的上下文继续执行

与generator

- 使用yield实现中断函数执行，且保留上下文
- 通过send()恢复函数执行
- 使用yield from实现任务嵌套
- 所以generator是可以作为协程来使用的

最简单的协程：generator-yield

```python
def corotine():
    for i in range(1000):
        try:
            a = yield i		# 中断执行
        except Exception as e:
            break
    return "over"

s = corotine()
for i in range(100):	
	s.send(None)	# 恢复执行
    if i == 10:
        try:
            s.throw(ZeroDivisionError)	# 结束执行
        except Exception as e:
            print(e.value)
    
# ---------
0
"over"
```

最简单的协程-完善

```python
import time

def corotine():
    for i in range(1000):
        try:
            print(i)	# 非堵塞逻辑
            yield time.sleep(1)	# 这里对于堵塞了
            print(i+1)	# 非堵塞逻辑
        except Exception as e:
            break
    return "over"

def task(name):
    print(f"{name} is executed")
    s = corotine()
    i = 1
    while True:
        print(s.send(None))    # 恢复执行
        if i == 10:
            try:
                s.throw(ZeroDivisionError)  # 结束执行
            except Exception as e:
                print(e.value)
                break
        i += 1

task("task1")
task("task2")


# ---------
task1 is executed
0
...
9
"over"
task2 is executed
0
...
9
"over"
```

最简单的协程-yield from

```python
import time

def corotine():
    for i in range(1000):
        try:
            a = yield i		# 中断执行
            time.sleep(1)	# 这里对于堵塞了
        except Exception as e:
            break
    return "over"

def task(name):
    # while True等价于yield from，都是遍历子任务
    yield from corotine()
```

最简单的协程-更新堵塞函数及其配套的event-loop

- 2.Future类，用于wrap异步函数
- 3.迭代执行函数schedule，loop.ready.append(future)
- 1.每个耗时对象会把自己添加进event-loop中，sleep()就是这样
  - 会创建自己的Future对象
  - 将自己的future对象加入event-loop
- 4.实际遍历执行异步任务的loop_task函数，遍历ready执行异步操作（用进程模拟其独立的执行）
  - execute函数，执行耗时操作，返回结果
  - 调用future对象绑定的callback，一般都是_wakeup，即解阻塞(自己所在协程的对象的iter方法，其中send(None))

```python
import time
from select import select
from multiprocessing import Process


ready = []

class Future:
    state = "pending"
    def __init__(self, coro):
        self.coro = coro

    def __call__(self, *args, **kwargs):
        result = self.coro(*args, **kwargs)
        self.state = "finish"
        return result

def execute(task, *args):
    result = task(*args)
    return result

def loop_task():
    while True:
        for task_info in ready:
            result = execute(task_info[0], task_info[1][1])
            callback = task_info[2]
            callback(task_info[1][0]:corotine, result)
        time.sleep(0.1)

# 调用时，注册异步任务后直接返回
def schedule(task, *context, callback=None):
    ready.append((task, context, callback))
    return

def wake_up(coro, result):
    coro.send(result)

# 异步任务，实现中需要将异步操作，回调函数加入到loop.ready中
def sleep(*args):
    # 1.将异步任务交给一个调度器
    # 2.绑定回调函数
    task = Future(time.sleep)
    schedule(task, *args, callback=wake_up)
    return task

# 实际会wrap成一个类，因为要传自己这个coroutine对象，之后调用send()给自己解阻塞
def coroutine(self):
    print(f"{self} is executed")

    for i in range(1000):
        # 对应task_new()
        # i == 10:
        #   return "over"
        try:
            # yield i		# 在正常的逻辑中，yield只会用在堵塞操作上
            print(i)        # 非阻塞业务逻辑
            wake = yield sleep(self, 5)         # 执行异步操作，用回调函数解阻塞接着完成子任务
            print(i+1)      # 非阻塞业务逻辑
        except Exception as e:
            break
    return "over"

if __name__ == '__main__':
    p1 = Process(target=loop_task)
    p2 = Process(target=task_new)
    p1.start()
    p2.start()
```

最简单的协程-更新task

```python
def task(name):
    # 但yield from还需要客户端遍历，但本质上coroutine是个任务
    # 所以把其当作一个完整的任务来看待
    await coroutine()

# 版本一：与asyncio顺序执行对应
def task(name):
    print("start")
    await corotine("task1")
    await corotine("task2")
    
# 版本二：与asyncio异步执行对应
def task_new():
    print("start")
    s1 = corotine("task1")
    s2 = corotine("task2")

    # 实际的业务逻辑中，下面的循环会仅相当于一个包含有堵塞操作的业务
    # (while True + 异常处理)的逻辑等价于yield from corotine()
    # 所以，总体等价于
    await s1
    await s2
```

最简单的协程-最终版

```python
import time
from select import select
from multiprocessing import Process


ready = []

class Future:
    state = "pending"
    def __init__(self, coro):
        self.coro = coro

    def __call__(self, *args, **kwargs):
        result = self.coro(*args, **kwargs)
        self.state = "finish"
        return result

def execute(task, *args):
    result = task(*args)
    return result

def loop_task():
    while True:
        for task_info in ready:
            result = execute(task_info[0], task_info[1][1])
            callback = task_info[2]
            callback(task_info[1][0]:corotine, result)
        time.sleep(0.1)

# 调用时，注册异步任务后直接返回
def schedule(task, *context, callback=None):
    ready.append((task, context, callback))
    return

def wake_up(coro, result):
    coro.send(result)

# 异步任务，实现中需要将异步操作，回调函数加入到loop.ready中
def sleep(*args):
    # 1.将异步任务交给一个调度器
    # 2.绑定回调函数
    task = Future(time.sleep)
    schedule(task, *args, callback=wake_up)
    return task

# 实际会wrap成一个类，因为要传自己这个coroutine对象，之后调用send()给自己解阻塞
def coroutine(self):
    print(f"{self} is executed")

    for i in range(1000):
        # 对应task_new()
        # i == 10:
        #   return "over"
        try:
            # yield i		# 在正常的逻辑中，yield只会用在堵塞操作上
            print(i)        # 非阻塞业务逻辑
            wake = yield sleep(self, 5)         # 执行异步操作，用回调函数解阻塞接着完成子任务
            print(i+1)      # 非阻塞业务逻辑
        except Exception as e:
            break
    return "over"

def task_new():
    print("start")
    s1 = corotine("task1")
    s2 = corotine("task2")
    
    await s1
    await s2

if __name__ == '__main__':
    p1 = Process(target=loop_task)
    p2 = Process(target=task_new)
    p1.start()
    p2.start()
```



对比

- asyncio，只执行加入到event-loop中的任务

  - 必须手动控制将任务加到循环中
  - 否则像版本一的写法，就不会是并发的执行

- 手动实现异步，可以用向上解阻塞的方式自动实现并发

  - 如：sleep阻塞，则使得task_new的s1任务解阻塞，从而实现在s1中阻塞时继续执行s2

  - 但是有问题：解阻塞向上走几层

    - 情况一：c1_1和c2_1不相关
    - 情况二：c1_1和c2_1相关
    - 那么，sleep阻塞导致c1_1解阻塞时，该继续向上解阻塞还是顺序执行

  - 所以，还是要手动控制，这样和asyncio就区别来，反正都要手动设置一下

    ```python
    def corotine_2():
        print("start")
        s = sleep("task1")
        print("end")
        
        await s
    
    def corotine_1():
        print("start")
        c1_1 = corotine_2("task1")
        c2_1 = corotine_2("task2")
        
        await c1_1
        await c2_1
        
    def main():
        print("start")
        s1 = corotine_1("task1")
        s2 = corotine_1("task2")
        
        await s1
        await s2
    ```




比较

- asyncio是完全基于事件循环的，如果没有添加进来，则不会执行
  - 需要手动的控制，添加异步到event_loop中
- 而自定义的异步协程，或者实现和asyncio的效果，或者向上解阻塞，但也要手动控制



参考：

- asyncio的历史：流畅的python(16章-协程，17章-future)

- [asyncio的历史：yield from&协程](https://juejin.im/post/6844903632534503437)






### TODO 并发：异步的方式写异步程序--->同步的方式写异步程序

概述

- aysnc+await，跑起来是异步的，但写起来感觉上是同步的



### 内置的concurrent模块

当前只有[concurrent.futures](https://docs.python.org/3.5/library/concurrent.futures.html#module-concurrent.futures)模块

> 从 Python3.2 开始一个叫做 concurrent.futures 被纳入了标准库，而在 Python2 它属于第三方的 futures 库，需要手动安装 

包含三个类：

- `concurrent.futures.Executor` 抽象基类
- `concurrent.futures.ThreadPoolExecutor` 线程池类
- `concurrent.futures.ProcessPoolExecutor` 进程池类

和threading/multiprocessing关系

- concurrent.futures 底层还是用着 threading 和 multiprocessing，相当于在其上又封装了一层 
- 是对 threading 和 multiprocessing 的进行了高级别的抽象， 暴露出统一的接口，帮助开发者非常方便的实现异步调用

参考：

- [使用Python进行并发编程-PoolExecutor篇](https://www.dongwm.com/post/78/)
- [使用concurrent.futures的一些经验](https://www.dongwm.com/post/use-concurrent-futures/)







