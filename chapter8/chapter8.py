# -*- coding:utf-8 -*-

#抛异常的时候，可以直接抛出一个类，会自动创建实例
#raise Exception

#也可以是提供一些说明信息的对象
#raise Exception('Error occured')

#内建异常类可以在exceptions模块中通过dir函数查看
#import exceptions
#print dir(exceptions)   #使用dir可以查看一个模块的内容

#创建自己的异常类，可以继承自exceptions类
class MyOwnException(Exception):
    pass
#raise MyOwnException

#异常可以上浮，如果要传递捕获的异常，可以使用不带参数的raise语句
#如果有多个异常要捕获，可以使用多个except子句
#如果对多个异常的处理方式类似，可以将多个异常放在元组中作为except子句的参数
#如果想要访问异常对象，可以为except子句提供两个参数
try:
    x = input("First number:")
    y = input("Second number:")
    print x / y
except (ZeroDivisionError, TypeError, NameError), e:
    print e

#使用没有参数的except子句可以捕获所有异常
