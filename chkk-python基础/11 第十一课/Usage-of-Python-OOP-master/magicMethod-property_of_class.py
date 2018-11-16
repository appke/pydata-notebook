#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

# python 一些magic method 提供类的属性操作的方法，其中包括但不限于：

# 魔术方法                              作用                                  重载的函数           调用方法
# __setattr__(self, name, value)        设置属性                                                   X.any = value
# __getattr__(self, name)               获取属性，仅当属性没有找到时调用      内建getattr()        X.undefined
# __getattribute__(self, name)          获取属性，总是被调用                  内建getattr()        X.any
# __delattr__(self, name)               删除属性                                                   del X.any

# 注意：以上这些魔术方法不能无限递归调用自身，因为python 的递归栈的深度限制为 1000
# 而__getattribute__方法更容易引起无限递归

# 接下来的实例展示如何进行类的属性操作


class Programmer(object):
    def __init__(self, name, age):  # 重写构造方法
        self.name = name  # 添加 name 属性
        self.age = age  # 添加 age 属性

    def __getattribute__(self, name):
        # return getattr(self, name)
        # return self.__dict__[name]
        return super(Programmer, self).__getattribute__(name)

    def __getattr__(self, name):
        return 'There is no property called %s here' % (name))

    def __setattr__(self, name, value):
        # setattr(self, name, value)
        self.__dict__[name] = value


if __name__ == '__main__':
    p = Programmer('Albert', 25)  # 实例化            调用了__init__方法
    print(p.name)  # 打印 name 属性                     调用了__getattribute__方法
    p.language = 'python'  # 添加 language 属性       调用了__setattr__方法
    print(p.language)  # 打印 language 属性             调用了__getattribute__方法
    del p.age  # 删除 age 属性                         调用了__delattr__方法，没有进行重写，直接继承自object类
    print(p.age)  # 打印 age 属性                       调用了__getattr__方法
    print(p.__dict__)  # 打印从构造函数里获得的属性     调用了__dict__方法
