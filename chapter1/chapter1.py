#! /usr/bin/env python
# #!称为pound bang或shebang
# -*- coding: utf-8 -*-

from __future__ import division
#Linux: $ python -Qnew

print 1 / 2         #0.5
print 1 // 2        #0
print 1.0 // 2.0    #0.0
print 2.75 % 0.5    #0.25
print -3 ** 2       #-9

#表达式有返回值，语句没有返回值
#解释器使用repr呈现结果

x = input('x:')     #input要求输入的是合法的python表达式，如2、"sample"
y = raw_input('y:') #raw_input自动将输入内容放在字符串中处理

print abs(-3.4)             #3.4
print abs(-4)               #4
print round(1.562345, 3)    #1.562
print round(1.562645, 3)    #1.563
print round(1.5, 3)         #1.5
print round(123.234, 0)     #123.0
print round(123.234, -1)    #120.0
print round(123.234, -2)    #100.0
print pow(2, 3, 5)          #3（2的3次方再对5取模）

import math
print math.floor(3)         #3.0
print math.floor(3.6)       #3.0
print math.ceil(3.6)        #4.0
print math.fabs(-4)         #4.0
#abs函数当参数为整数时返回整数，参数为浮点数时返回浮点数
#math.fabs函数始终返回浮点数

foo = math.sqrt
print foo(4)                #2.0

import cmath
print cmath.sqrt(-3)        #1.73205080757j

#为了避免import冲突，最好坚持使用import，不使用from..import..的形式
#import this可以看到python的哲学

#print展现便于人阅读的结果，使用str
#repr力求保持值在代码中的状态

#记得有原始字符串这回事！可用于正则表达式
print r'C:\Users\Admins\Downloads\a.pdf' #C:\Users\Admins\Downloads\a.pdf
#原始字符串中，最后一个字符不能是\
print R'D:\Program' '\\'                 #D:\program\

print len('卢mz')           #5
print len(u'卢mz')          #3
