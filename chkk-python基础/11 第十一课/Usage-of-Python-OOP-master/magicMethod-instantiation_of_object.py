#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

# 对象实例化的过程：
# 创建类的对象（__new__(cls) 会返回一个类的初始对象）-----> 初始化对象（__init__(self) 对初始对象的属性进行设置）

# 销毁对象的过程：
# 在垃圾回收的时候会调用__del__() 一般不需要自己定义

# 接下来的实例展示如何自定义类的__new__和__init__方法


class Programmer(object):
    def __new__(cls, *args, **kwargs):  # 返回一个类的初始对象
        print('call __new__ method')
        print(args)  # 打印传入的参数
        return super(Programmer, cls).__new__(cls)  # 调用父类的同名方法返回对象
        #return object.__new__(cls)

    def __init__(self, name, age):  # 对初始对象的属性进行设置
        print('call __init__ method')
        self.name = name
        self.age = age


if __name__ == '__main__':
    programmer = Programmer('Albert', 25)  # 实例化的过程中先__new__后__init__
    print(programmer.__dict__)  # 从构造函数里获得的属性)
