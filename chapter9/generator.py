# -*- coding:utf-8 -*-

#生成器：包含yield语句的函数成为生成器
#调用这个函数时，并不执行函数体中的代码，而是返回一个迭代器
#每次请求一个值，会执行函数体中的代码，直到遇到一个yield语句或return语句
#如果遇到yield语句，生成一个值，冻结函数，下次调用时继续执行函数
#如果遇到无参数return语句，直接返回，停止执行函数体
#只有在生成器的定义中可以使用无参数的return语句
#展开列表的列表的生成器
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element

for item in flatten([[2, 3], [4], [9, 4, 1]]):
    print item,             #2 3 4 9 4 1
print 

#对于需要大量迭代的值，可以使用生成器推导式完成，比如：
g = (i**2 for i in xrange(100000))
print g.next()              #0

#展开任意层嵌套列表的生成器
def flatten2(nested):
    try:
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flatten2(sublist):
                yield element
    except TypeError:
        yield nested


for item in flatten2([[2, [2, 'abc', 3], 3], [4], [9, 4, 1]]):
    print item,             #2 2 abc 3 3 4 9 4 1
print 

def sample():
    for i in range(10):
        if i == 7:
            return
        yield i

print list(sample())        #[0, 1, 2, 3, 4, 5, 6]
