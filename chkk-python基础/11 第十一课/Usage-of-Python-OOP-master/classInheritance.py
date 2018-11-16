#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 在python2 中如果不用继承任何类，最好继承object 类
# python 支持多继承，一般用不到

# 接下来的实例展示类的继承


class Programmer(object):
    hobby = 'Play Computer'  # 类属性，在每个实例中相同

    def __init__(self, name, age, weight):
        self.name = name  # 公开属性
        self._age = age  # 一般表示私有属性，但是可以在类外直接访问
        self.__weight = weight  # 表示私有属性，不能在类外直接访问

    @classmethod  # 类方法：方法的装饰器，类似于类属性，直接用类名调用，不需要生成对象  Programmer.get_hobby()
    def get_hobby(cls):
        return cls.hobby

    @property  # 属性方法：方法的装饰器，调用方法与构造方法中的属性相同，不需要加括号  programmer.get_weight
    def get_weight(self):
        return self.__weight

    def self_introduction(self):  # 一般的方法，用object.method()的方法调用  programmer.self_introduction()
        print('My name is %s.I am %s years old.' % (self.name, self._age))


class BackendProgrammer(Programmer):  # BackendProgrammer 类继承自Programmer 类
    def __init__(self, name, age, weight, language):  # 重写构造方法
        super(BackendProgrammer, self).__init__(name, age, weight)  # 调用父类的构造方法
        self.language = language  # 子类特性


if __name__ == '__main__':
    programmer = BackendProgrammer('Albert', 25, 80, 'python')  # 实例化
    print(dir(programmer))  # 输出所有属性
    print(programmer.__dict__)  # 从构造函数里获得的属性
    print(type(programmer))  # 返回对象的类
    print(isinstance(programmer, Programmer))  # programmer 是否是 Programmer 类的一个对象
