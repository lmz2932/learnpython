# -*- coding: utf-8 -*-

#定义对象的构造方法__init__
#对象的析构方法__del__的调用时间未知，所以一般不要重定义__del__方法
class Sample(object):
    def __init__(self, value = 42):
        self.value = value

a = Sample()
print a.value                   #42
b = Sample('Mars Loo')
print b.value                   #Mars Loo

#继承的过程中重写基类的方法
class A(object):
    def hello(self):
        print 'Hello, I\'m A'

class B(A):
    pass

a = A()
b = B()
a.hello()                       #Hello, I'm A
b.hello()                       #Hello, I'm A

class B(A):
    def hello(self):
        print 'Hello, I\'m B'

a = A()
b = B()
a.hello()                       #Hello, I'm A
b.hello()                       #Hello, I'm B

#如果重定义了子类的构造方法，那么一定要在定义时调用基类的构造方法
#否则子类不会被正确的初始化
#1.调用基类的未绑定方法
class Bird(object):
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print 'Ehhhh...'
            self.hungry = False
        else:
            print 'I\'m full, thanks!'

class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.song = 'Squark'
    def sing(self):
        print self.song

sb = SongBird()
sb.eat()                    #Ehhhh...
sb.sing()                   #Squark
sb.eat()                    #I'm full, thanks!
#2.新式类使用super函数，即使有多重继承也能找到正确的构造方法
#（前提是这些类都使用了super函数处理构造方法）
class SongBird2(Bird):
    def __init__(self):
        super(SongBird2, self).__init__()
        self.song = 'Squark'
    def sing(self):
        print self.song

sb = SongBird2()
sb.eat()                    #Ehhhh...
sb.sing()                   #Squark
sb.eat()                    #I'm full, thanks!

#一些Python类的规则
#__len__(self):返回集合中元素的数量（可变、不可变）
#__getitem__(self, key):返回键对应的值（可变、不可变）
#__setitem__(self, key, value):为某个键赋值（可变）
#__delitem__(self, key):删除某个键及对应的值（可变）

#子类化内建类
class CounterList(list):
    def __init__(self, *args):
        super(CounterList, self).__init__(*args)
        self.counter = 0
    def __getitem__(self, key):
        self.counter += 1
        return super(CounterList, self).__getitem__(key)

c1 = CounterList([2, 3, 5, 1])
print c1[2] + c1[0]         #7
print c1.counter            #2

#属性property
#通过访问器定义的特性称为属性
class Rectangle(object):
    def __init__(self):
        self.width = 0
        self.height = 0

    def get_size(self):
        return self.width, self.height

    def set_size(self, size):
        self.width, self.height = size
    
    def del_size(self):
        self.__init__()

    size = property(fget = get_size, fset = set_size, fdel = del_size)

rt = Rectangle()
rt.set_size((2, 3))
print rt.get_size()         #(2, 3)
print rt.width, rt.height   #2 3
print rt.size               #(2, 3)
rt.size = (3, 4)
print rt.get_size()         #(3, 4)
del rt.size
print rt.get_size()         #(0, 0)

#property函数的四个参数：
#property(fget = None, fset = None, fdel = None, doc = None)

#staticmethod和classmethod
#1.如果要再外部操作一个类，可以定义一个函数操作这个类，
#不过在这个类中定义一个classmethod会更好
class Sample(object):
    counter = 0

    def __init__(self):
        Sample.counter += 1

    @classmethod
    #classmethod的特点是，第一个参数是自动绑定的类
    def get_counter(cls):
        print cls.counter

a = Sample()
a.get_counter()             #1
b = Sample()
Sample.get_counter()        #2
#2.staticmethod也用于同样的场景，不同是不强制有参数
DB = 'mysql'
class Sample2(object):
    @staticmethod
    def get_db():
        return DB

    def connect(self):
        db = self.get_db()
        print 'connect to %s done' % db

c = Sample2()
c.connect()                 #connect to mysql done

#拦截对类成员的访问
#1.__getattribute__用来拦截对所有attribute（不管是否存在）的访问--新式类才有
#2.__getattr__当访问不存在的attribute时被调用--新式类或旧式类
#3.__setattr__对attribute赋值时被调用--新式类或旧式类
class Sample3(object):
    def __getattr__(self, name):
        print '__getattr__'
        return None

    def __setattr__(self, name, value):
        print '__setattr__'
        #不直接使用self.name是为了避免循环调用__setattr__方法
        self.__dict__[name] = value

    def __getattribute__(self, name):
        print '__getattribute__'
        try:
            #因为__getattribute__会拦截__dict__，所以需要使用其基类的__getattribute__方法
            return super(Sample3, self).__getattribute__(name)
        except AttributeError:
            print 'Caught attribute error'

a = Sample3()
a.x
#__getattribute__
#Caught attribute error
a.x = 3
#__setattr__
#__getattribute__
a.x
#__getattribute__

#自定义可迭代对象
#实现了__iter__方法的对象是可迭代的，实现了next方法的对象称为迭代器
class Fib(object):
    def __init__(self):
        self.a, self.b = 1, 1

    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.a + self.b, self.a
        return self.a

for f in Fib():
    print f
    if f > 10:
        break
#2
#3
#5
#8
#13

f = Fib()
print f.next()      #2
print f.next()      #3

class Fib2(Fib):
    def next(self):
        self.a, self.b = self.a + self.b, self.a
        if self.a > 10:
            raise StopIteration
        return self.a

f2 = Fib2()
print list(f2)      #[2, 3, 5, 8]
