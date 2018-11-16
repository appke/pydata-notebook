#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 多态可以用来表示不同的人对相同事物的看法不用，或做同一事情的方法不同等等

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
        print('My name is %s. I am %s years old.' % (self.name, self._age))


class BackendProgrammer(Programmer):  # BackendProgrammer 类继承自Programmer 类
    def __init__(self, name, age, weight, language):  # 重写构造方法
        super(BackendProgrammer, self).__init__(name, age, weight)  # 调用父类的构造方法
        self.language = language  # 子类特性

    def self_introduction(self):  # 重写self_introduction 方法
        print('My name is %s. My favourite language is %s.' % (self.name, self.language))


def introduce(programmer):  # 自我介绍
    if isinstance(programmer, Programmer):
        programmer.self_introduction()  # 多态：不同种类的programmer 进行self_introduction 时有不同的表现


if __name__ == '__main__':
    programmer = Programmer('Albert', 25, 80)  # 创建Programmer 类的对象
    backend_programmer = BackendProgrammer('Tim', 30, 70, 'python')  # 创建BackendProgrammer 类的对象
    introduce(programmer)  # programmer 自我介绍
    introduce(backend_programmer)  # backend_programmer 自我介绍
