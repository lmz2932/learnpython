#!/usr/bin/env python
# -*- coding:utf-8 -*-

a = [('name', 'mars'), ('age', 23)]
b = dict(a)
print b             #{'age': 23, 'name': 'mars'}
c = dict(name = 'suson', age = 25)
print c             #{'age': 25, 'name': 'suson'}

d = '%(name)s is beautiful!'
e = {
    'name': 'flower',
    'age': 23,
}
print d % e         #flower is beautiful!

f = {'x': 'name', 'y': [12, 34, 56]}
g = f.copy()        #字典的copy方法是浅复制
g['x'] = 'age'
g['y'].remove(12)
print f             #{'y': [34, 56], 'x': 'name'}
print g             #{'y': [34, 56], 'x': 'age'}

from copy import deepcopy
h = deepcopy(g)
h['y'].remove(56)
print g             #{'y': [34, 56], 'x': 'age'}
print h             #{'y': [34], 'x': 'age'}

i = {}.fromkeys(['name', 'age'])
print i             #{'age': None, 'name': None}
j = dict.fromkeys(['name', 'age'], 'Unkown')
print j             #{'age': 'Unkown', 'name': 'Unkown'}

k = {'name': 'loo', 'length': 23}
print k.get('age')  #None
#iteritems,iterkeys,itervalues返回的是迭代器
print list(k.iteritems())           #[('length', 23), ('name', 'loo')]
print list(k.iterkeys())            #['length', 'name']
print list(k.itervalues())          #[23, 'loo']
print k.pop('length')               #23
print k                             #{'name': 'loo'}
print j.popitem()                   #('age', 'Unkown')，popitem是随机的弹出
print j                             #{'name': 'Unkown'}
k.setdefault('car')
print k                             #{'car': None, 'name': 'loo'}
k.update({'car': 'bmw', 'age': 23})
print k                             #{'car': 'bmw', 'age': 23, 'name': 'loo'}
