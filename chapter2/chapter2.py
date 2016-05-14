#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print a[ : : 4]             #[1, 5, 9]
print a[8 : 2 : -3]         #[9, 6]
print a[10 : 2 : -3]        #[10, 7, 4]

a[2 : 2] = [123]            #相当于插入
print a     #[1, 2, 123, 3, 4, 5, 6, 7, 8, 9, 10]
a[2 : 3] = []               #相当于删除
print a     #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a[2 : 3] = [2]              #相当于替换
print a     #[1, 2, 2, 4, 5, 6, 7, 8, 9, 10]
print a.pop()               #10
print a.pop(1)              #2
print a     #[1, 2, 4, 5, 6, 7, 8, 9]
a.insert(1, 3)
print a     #[1, 3, 2, 4, 5, 6, 7, 8, 9]
result = a.sort()           #默认从小到大排序
print a, result             #[1, 2, 3, 4, 5, 6, 7, 8, 9] None
a[0] = 100
result = sorted(a)
print a, result             #[100, 2, 3, 4, 5, 6, 7, 8, 9] [2, 3, 4, 5, 6, 7, 8, 9, 100]

b = {
    'name': 'mars loo',
    'age': 25
}
print max(b)                #name //比较的是字典的键

try:
    #value = 321
    value = 2
    idx = a.index(value)
except:
    print value, 'not found!'
else:
    print "%d's index:%d." % (value, idx)
finally:
    print "Thank you!"

try:
    value = 'd'
    #value = 'a'
    c = list('have')
    c.remove(value)
except:
    print value, 'not found!'
else:
    print c

d = ['This', 'is', 'a', 'sample']
print d.sort(key = len), d      #None ['a', 'is', 'This', 'sample']
print d.sort(key = len, reverse = True), d  #None ['sample', 'This', 'is', 'a']
#list.sort(cmp = None, key = None, reverse = None)
print cmp(1, 2), cmp(1, 1), cmp(2, 1)       #-1 0 1

def mycmp(a, b):
    return -cmp(a, b)

print d.sort(cmp = mycmp),d                 #None ['sample', 'is', 'a', 'This']
