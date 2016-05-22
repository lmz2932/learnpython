# -*- coding:utf-8 -*-

print bool("")              #False

#如下比较的前提是类型相同
x, y = 1, 2
print x ==y                 #False
print x > y                 #False
print x >= y                #False
print x < y                 #True
print x <= y                #True

print ord('a')              #97
print chr(65)               #A

#迭代工具
a = range(5)
b = xrange(10000)
print zip(a,b)              #[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

age = -1
#assert 0 <= age <= 100, "Age should between [0, 100]"
c = ["a", "d", "c"]
for index,value in enumerate(c):
    print index,value      
#0 a
#1 d
#2 c

print sorted(c)             #['a', 'c', 'd']
print list(reversed(c))     #['c', 'd', 'a'],reversed方法返回一个可迭代对象

for i in range(100, 90, -1):
    if i == 90:
        break
else:                       #else子句适用于for、while循环,在内部没有发生break的时候执行
    print 'I never break!'  #'I never break!'

print [(x, y) for x in range(10) for y in range(10) if x == y ** 2]
#[(0, 0), (1, 1), (4, 2), (9, 3)]

def func():                 #使用docstring可以替代pass语句占位
    '''
        This is the docstring
    '''

exec "print 'Hello world!'" #Hello world!
s = {}                      #命名空间
exec "a = 2" in s
print s.keys()              #['__builtins__', 'a'] 
exec "b = 3" in s
print eval("a*b", s)        #6
