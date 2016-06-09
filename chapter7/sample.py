# -*- coding:utf-8 -*-

#使用下划线隐藏内部变量和方法，在from module import *时是生效的

_not = '0'
yes = 1

def _inner():
    print 'This is inner'

def outer():
    print 'This is outer'

#>>> from sample import *
#>>> print _not
#Traceback (most recent call last):
#      File "<stdin>", line 1, in <module>
#      NameError: name '_not' is not defined
#>>> print yes
#1
#>>> _inner()
#Traceback (most recent call last):
#    File "<stdin>", line 1, in <module>
#    NameError: name '_inner' is not defined
#>>> outer()
#This is outer
