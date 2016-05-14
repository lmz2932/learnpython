#!/usr/bin/env python
# -*- coding:utf-8 -*-

from math import pi

print '**********'                  #**********（长度为10）
print "%10.3f" % pi                 #3.142，默认为右对齐,小数点后数字表示精度
print '%-10d' % 3                   #-左对齐，10最小字段宽度
print '%0*d' % (10, 3)              #0在值前面填充零,*最小字段宽度从元组中读取
print '%+i,%+i' % (-3, 4)           #+在值前面加上正负号,i带符号十进制正数
print '% 2d' % 3                    #' '在正数前面保留空格
print '% 2d' % -3
print '%.3s' % 'abcd'               #小数点后数字表示最大长度

import string

s = string.Template('$x, $$ ${y}tastic!')
print s.substitute(x = 'mars', y = 'loo')   #mars, $ lootastic!
d = { 'x' : 123 }
print s.safe_substitute(d)                  #123, $ ${y}tastic!
print string.digits                 #0123456789
print string.ascii_letters          #返回所有大小写字母
print string.lowercase              #返回所有小写字母
print string.uppercase              #返回所有大写字母
print string.punctuation            #返回所有标点符号
print string.printable              #返回所有可打印字符

#value = 'avc'
value = 'abc'
if 'avc is a test'.find(value) >= 0:
    print value, 'was found.'
else:
    print value, 'not found.'
print 'avc is a test'.find(value, 4, 10)

print 'Haha, This is.'.lower()              #haha, this is.
print "This's a test.".title()              #This'S A Test.
print string.capwords("This's a test.")     #This's A Test.
print ' *~This has.&%*'.strip(' *~&%')      #This has.
#replace每次调用只能替换一个'单词'
print 'Suson loves cookie.'.replace('cookie', 'Mars') #Suson loves Mars.
#translate每次调用可以替换多个'字符'
#调用时除了要替换的映射以外，还需要提供其它所有字符的映射
#所以直接使用string.maketrans制作映射表比较好
table = string.maketrans('jsx', '*&^')
print 'This jar of box.'.translate(table)   #Thi& *ar of bo^.
#translate也可以在转换的过程中直接删除一部分转换前的字符
print 'This jar of box.'.translate(table, ' ') #Thi&*arofbo^.
