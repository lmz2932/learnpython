# 简介
Python笔记归档，需要时供查询使用

## concurrency目录
Python并发编程方法总结。

### multiprocessing
使用multiprocessing包进行多进程编程，[CSDN博客](http://blog.csdn.net/a464057216/article/details/52735584)。

#### 1.py
使用Process对象创建进程，获取进程ID及父进程ID。

#### 2-1.py
进程间通信（使用Queue）。

#### 2-2.py
进程间通信（使用Pipe）。

#### 3.py
加锁处理。

#### 4-1.py
使用共享内存实现进程间共享状态。

#### 4-2.py
使用服务进程实现进程间共享状态。

#### 4-3.py
使用共享内存及服务进程共享状态，一定要加锁。

#### 4-4.py
进程间普通内存变量不共享的例子。

#### 5.py
使用进程池。

#### 6-1.py
例子：使用Process对象实现指定并发的HTTP Web API测试。

#### 6-2.py
例子：使用进程池实现指定并发的HTTP Web API测试。

### threading
使用Python的threading包完成多线程编程,[CSDN博客]()。

#### 1.py
使用Thread对象创建线程并执行。

#### 2.py
守护线程与获取线程名字。

#### 3.py
使用互斥锁Lock访问线程间共享变量，通过类的方式定义线程。

#### 4.py
多线程死锁示例。

#### 5.py
可重入锁RLock。

#### 6.py
通过条件对象Condition实现复杂锁场景，“生产者-消费者”模型。

#### 7.py
使用信号量Semaphore实现并发控制。

#### 8.py
使用事件对象Event进行线程间的通信。

#### 9.py
使用Timer对象定时执行线程。
