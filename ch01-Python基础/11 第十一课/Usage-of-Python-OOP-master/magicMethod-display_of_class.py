#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

# python 一些magic method 提供把对象转换为字符串的方法，其中包括但不限于：

# 魔术方法          作用                        重载的函数
# __str__           可打印的字符输出            内建str()及print 语句
# __repr__          运行时的字符串输出          内建repr()
# __unicode__       Unicode 字符串输出          内建unicode()
# __dir__           查看对像内所有属于及方法    内建dir()

# 接下来的实例展示如何进行运算符的重载


class Programmer(object):
    def __init__(self, name, age):  # 重写构造方法
        self.name = name  # 添加 name 属性
        if isinstance(age, int):  # 如果 age 属于 int 类
            self.age = age  # 添加 age 属性
        else:  # 否则
            raise Exception('Age must be int')  # 抛出异常

    def __str__(self):  # 重载内建str()及print 语句
        return('%s is %s years old' % (self.name, self.age))

    def __dir__(self):  # 重载内建dir()
        return self.__dict__.keys()


if __name__ == '__main__':
    p = Programmer('Albert', 25)  # 实例化
    print(p)  # 打印 p 对象
    print(dir(p))  # 打印 dir(p)
