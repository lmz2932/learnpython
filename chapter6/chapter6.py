# -*- coding:utf-8 -*-

def func():
    '''
        A sample function docstring.
    '''
    print 'This is a function'
x = 1

#callable适用于python 2.x，python 3.x需要使用hasattr(func, __call__)
print callable(func)        #True
print callable(x)           #False

print func.__doc__          #A sample function docstring.
help(func)                  #Enter the help documentation for func

#定义函数时，*param将剩余位置参数收集为元组，**param将剩余关键字参数收集为字典
#调用函数时，*param将元组解开为位置参数，**param将字典解开为关键字参数
def welcome(greeting, *param):
    print greeting + '!', ','.join(param) + '.'

welcome('haha', 'mars', 'suson')        #haha! mars,suson.
guests = ['Tom', 'Mei']
welcome('welcome', *guests)             #welcome! Tom,Mei.

def mmath(**param):
    print '*'.join(param.keys()), '=',
    r = 1
    for value in param.values():
        r *= value
    print r

mmath(x = 1, y = 2)         #y*x = 2
d = {
    'a': 2,
    'b': 3,
    'c': 4
}
mmath(**d)                  #a*c*b = 24

#局部作用域调用vars函数，返回局部命名空间字典
#全局作用域调用vars函数，返回全局命名空间字典
#vars函数返回的结果不可更改
print 'global:', vars()
#global: {'mmath': <function mmath at 0x10e2ec758>, '__builtins__': <module '__builtin__' (built-in)>, '__file__': 'chapter6/chapter6.py', 'welcome': <function welcome at 0x10e4c4500>, '__package__': None, 'guests': ['Tom', 'Mei'], 'func': <function func at 0x10e2e9c80>, 'x': 1, '__name__': '__main__', '__doc__': None, 'd': {'a': 2, 'c': 4, 'b': 3}}

def a():
    x = 1
    print 'Local:', vars()

a()                         #Local: {'x': 1}

#函数内部使用全局变量可以使用globals函数引用
#虽然可以直接使用变量的名字，但是使用globals可以强调全局属性
def global_in_local():
    gd = globals()['d']
    print gd
    print d
global_in_local()
#{'a': 2, 'c': 4, 'b': 3}
#{'a': 2, 'c': 4, 'b': 3}

a = [2, 3]
b = [5, 7]
def func(x, y):
    return x * y
print map(func, a, b)       #[10, 21]
print map(str, range(5))    #['0', '1', '2', '3', '4']
#filter可以基于一个返回布尔值的函数对元素进行过滤
def is_even(x):
    return x % 2 == 0
print filter(is_even, [5, 2, 4, 6, 3, 2])       #[2, 4, 6, 2]
print filter(lambda x: x.isalnum(), ['2', '#$', 'as2'])       #['2', 'as2']
#reduce会将序列中第1、2个元素作为函数参数输入，取输出与第3个元素再作为
#函数参数输入，以此类推，最后返回函数输出
print reduce(lambda x, y: x + y, [1, 2, 3])     #6
print reduce(lambda x, y: x + y, [1,])          #1

print sum([3, 1, 2], 4)     #10
def sample(x, y, a = 1, b = 3):
    print x, y
    print a * b
li = ['Mars', 'Loo']
di = {
        'a': 3,
        'b': 9
    }
apply(sample, li, di)
#Mars Loo
#27
