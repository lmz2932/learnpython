# 简介
Python笔记归档，需要时供查询使用

## concurrency目录
Python并发编程方法总结。

### multiprocessing
使用multiprocessing包进行多进程变成，[CSDN博客]()。

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
