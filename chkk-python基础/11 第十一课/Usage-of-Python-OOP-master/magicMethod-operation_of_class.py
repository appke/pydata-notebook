#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

# python 一些magic method 提供对运算符的重载，其中包括但不限于：

# 比较运算符：
# __cmp__(self, other)      重载 cmp(a, b) 函数
# __eq__(self, other)       等于（定义好之后两个对象才能做等于(==)的判断，下面的类似）
# __lt__(self, other)       小于
# __gt__(self, other)       大于

# 数字运算符：
# __add__(self, other)      加 （定义好之后两个对象才能做加法(+)运算，下面的类似）
# __sub__(self, other)      减
# __mul__(self, other)      乘
# __div__(self, other)      除

# 逻辑运算符：
# __or__(self, other)       或 （定义好之后两个对象才能做或(or)运算，下面的类似）
# __and__(self, other)      与

# 接下来的实例展示如何进行运算符的重载


class Programmer(object):
    def __init__(self, name, age):  # 重写构造方法
        self.name = name  # 添加 name 属性
        if isinstance(age, int):  # 如果 age 属于 int 类
            self.age = age  # 添加 age 属性
        else:  # 否则
            raise Exception('Age must be int')  # 抛出异常

    def __eq__(self, other):  # 重载 = 和 !=
        if isinstance(other, Programmer):  # other 对象也属于 Programmer 类
            if self.age == other.age:  # 判断两个对象是否相等的条件是判断两个对象的 age 属性是否相等
                return True
            else:
                return False
        else:  # 如果other 对象不属于 Programmer 类
            raise Exception('The type of object must be Programmer')  # 抛出异常

    def __add__(self, other):  # 重载 +
        if isinstance(other, Programmer):  # other 对象也属于 Programmer 类
            return self.age + other.age  # 两对象相加返回 age 属性的和
        else:  # 如果other 对象不属于 Programmer 类
            raise Exception('The type of object must be Programmer')  # 抛出异常


if __name__ == '__main__':
    p1 = Programmer('Albert', 25)  # 实例化
    p2 = Programmer('Bill', 30)  # 实例化
    print(p1 == p2)  # 打印 p1 == p2 的结果
    print(p1 + p2)  # 打印 p1 + p2 的结果
