#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

# 在python2 下运行经典类和新式类会有区别，因为python2 下的类不会默认继承object 类，只有显式继承了object 才是新式类

# 接下来的实例展示如何定义类


class OldStyle: # python2 中的类默认为经典类
    def __init__(self, name, description):
        self.name = name
        self.description = description


class NewStyle(object): # 只有显式继承object 的才是新式类
    def __init__(self, name, description):
        self.name = name
        self.description = description


if __name__ == '__main__':
    old = OldStyle('old', 'Old style class')
    print(old)
    print(type(old))
    print(dir(old))
    print('--------------------------------------------------------------------')
    new = NewStyle('new', 'New style class')
    print(new)
    print(type(new))
    print(dir(new))
