# -*- coding:utf-8 -*-

#对象是属性attribute和方法method的集合，是类的实例instance
#面向对象的特点：封装、继承、多态
#使用新式类也可以继承自object，新式类声明一般放在脚本或模块的开始
__metaclass__ = type    #使用新式类

class Person:
    def set_name(self, name):
        self.name = name

    def get_name(self):     #称为访问器accessor
        return self.name

    def greet(self):
        print "Hello, world! I'm %s." % self.name

mars = Person()
mars.set_name('mars')
print Person.get_name(mars) #mars
print mars.name             #mars
mars.name = 'suson'
mars.greet()                #Hello, world! I'm suson.

#上例中，直接通过mars.name修改类的私有变量是非常危险的
#所以程序员约定在变量或方法名前面加一条下划线表示是私有的（仅仅是个约定）
#这种约定在from module import *的时候奏效，不过其实仍然可以通过名字访问

class Bird:
    _song = 'BiuBiu~~'
    def sing(self):
        print self._song

a = Bird()
a.sing()                    #BiuBiu~~
print a._song               #BiuBiu~~

#如果加上两个下划线，看起来好像变成了私有，不过其实还是可以访问到的
class Secret:
    __passwd = 'very secure'
    def get_passwd(self):
        print self.__passwd

b = Secret()
try:
    print b.__passwd
except:
    print "Can't access via __passwd"
#Can't access via __passwd
print b._Secret__passwd     #very secure

#如下两种定义几乎是等价的
def foo(x): return x * x
foo2 = lambda x: x * x
print foo(3)
print foo2(3)

#类的定义也可以执行其他的语句
class Sample:
    print 'Created a instance of Sample'
a = Sample()                #Created a instance of Sample

#在类中定义的属性所有实例可访问
#如果直接修改某个实例的该属性，则修改后的值仅该实例可见，其他实例仍然使用类属性
class Counter:
    members = 0
    def init(self):
        Counter.members += 1
a, b = (Counter(), Counter())
a.init(), b.init()
print a.members, b.members  #2 2
a.members = 'Three'
print a.members, b.members  #Three 2

import random
print random.choice([1, 2, 4])  #可能是1，2或者4

#指定超类
class Filter():
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']

a = Filter()
a.init()
print a.filter(['SPAM', 'mars', 'loo']) #['SPAM', 'mars', 'loo']
b = SPAMFilter()
b.init()
print b.filter(['SPAM', 'mars', 'loo']) #['mars', 'loo']
#子类判断及查询基类
print issubclass(SPAMFilter, Filter)    #True
print SPAMFilter.__bases__              #(<class '__main__.Filter'>,)
print Filter.__bases__
#对象类型判断
print isinstance(b, SPAMFilter)         #True
print isinstance(b, Filter)             #True
print b.__class__                       #<class '__main__.SPAMFilter'>
print type(b)                           #<class '__main__.SPAMFilter'>

#多重继承
class Calculator():
    def calculate(self, expression):
        self.value = eval(expression)

class Talker():
    def talk(self):
        print 'My value is', self.value

class TalkingCalculator(Calculator, Talker):
    pass

tc = TalkingCalculator()
tc.calculate('1 + 2 * 3')
tc.talk()                               #My value is 7

#类的特性检查
print hasattr(tc, 'calculate')          #True
print hasattr(tc, 'cal')                #False
print callable(getattr(tc, 'value', None))      #False
setattr(tc, 'new', 'mars')
print tc.new                            #mars
print tc.__dict__                       #查看对象内所有属性值
