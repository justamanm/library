[gevent由来-csdn](https://blog.csdn.net/gzlaiyonghao/article/details/7218611)

> I/O 方面，多线程帮助有限，以 TCP Socket Server 为例，如果每一个 client connection 由一条专属的线程服务，那么这个 server 可能并发量很难超过 1000。
>
> 为了进一步解决并发带来的问题，现代服务器都使用 event-driven i/o 了。 
>
> event-driven i/o 解决了并发量的问题，但引入了“代码被回调函数分割得零零碎碎”的问题。特别是当 event-driven i/o 跟 multi-threading 结合在一起的时候，麻烦就倍增了。
>
> 解决这个问题的办法就使用绿色线程，绿色线程可以在同一个进程中成千上万地存在，从而可以在异步 I/O 上封装出同步的 APIs，典型的就是用基于 greenlet + libevent 开发的 python 库 gevent。
>
> 绿色线程的缺陷在于操作系统不知道它的存在，需要用户进行调度，也就无法利用到多核或多路 CPU 了。
>
> 为了解决这个问题，很多大牛都做出了巨大的努力，并且成果斐然，scala、google go 和 rust 都较好地解决了问题，下文以 rust 的并发模型为例讲一下。 
>
> rust 提出一个 Task 的概念，Task 有一个入口函数，也有自己的栈，并拥有进程堆内存的一部分，为方便理解，你可以把它看作一条绿色线程。rust 进程可以创建成千上万个 Tasks，它们由内建的调度器进行调度，因为 Tasks 之间并不共享数据，只通过 channels/ports 通信，所以它们是可并行程度很高。
>
> rust 程序启动时会生成若干条（数量由 CPU 核数决定或运行时指定）线程，这些线程并行执行 Tasks，从而利用多个 CPU 核心。 



基于greenlet + libevent