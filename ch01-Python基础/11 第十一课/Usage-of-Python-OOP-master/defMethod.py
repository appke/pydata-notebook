#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

# python 类中的方法与属性相同，不提供访问控制的功能，所以一样需要用下划线进行访问控制
# 还有两种方法的装饰器 @classmethod @property 具体使用方法见代码

# 接下来的实例展示如何定义类的方法


class Programmer(object):
    hobby = 'Play Computer'  # 类属性，在每个实例中相同

    def __init__(self, name, age, weight):
        self.name = name  # 公开属性
        self._age = age  # 一般表示私有属性，但是可以在类外直接访问
        self.__weight = weight  # 表示私有属性，不能在类外直接访问

    @classmethod # 类方法：方法的装饰器，类似于类属性，直接用类名调用，不需要生成对象  Programmer.get_hobby()
    def get_hobby(cls):
        return cls.hobby

    @property # 属性方法：方法的装饰器，调用方法与构造方法中的属性相同，不需要加括号  programmer.get_weight
    def get_weight(self):
        return self.__weight

    def self_introduction(self): # 一般的方法，用object.method()的方法调用  programmer.self_introduction()
        print 'My name is %s.I am %s years old.' % (self.name, self._age)


if __name__ == '__main__':
    programmer = Programmer('Albert', 25, 80)  # 实例化
    print(dir(programmer))  # 输出所有属性
    print(Programmer.get_hobby()) # 调用类方法
    print(programmer.get_weight) # 调用属性方法
    programmer.self_introduction() # 调用一般方法
