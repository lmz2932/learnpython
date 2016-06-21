# -*- coding:utf-8 -*-

class C(object):
    def __init__(self):
        self._x = None
    
    def setx(self, value):
        self._x = value

    def getx(self):
        return self._x

    def delx(self):
        del self._x

    x = property(fget = getx, fset = setx, fdel = delx, doc = "I'm property x")
#>>> from property import C
#>>> help(C)

#如果doc未提供，会使用fget参数的docstring
class D(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        '''
            return the value of x
        '''
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self.x
