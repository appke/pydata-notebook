#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

# 类中定义的属性在每一个对象中都一样
# 构造函数中定义的属性在实例化的时候才进行赋值，是可以不同的

# python 本身不提供访问控制的功能，但是可以用一些小技巧达到私有属性的效果。
# 为了让方法或者属性变为私有（从外部无法访问），只要在它的名字前面加上双下划线即可。
# 类的内部定义中，所有以双下划线开始的名字都被“翻译”成前面加上单下划线和类名的形式。
# 在了解了这些幕后的事情后，实际上还是能在类外访问这些私有方法，尽管不应该这么做：
# print  programmer._Programmer__weight

# 接下来的实例展示如何定义类的属性


class Programmer(object):
    hobby = 'Play Computer' # 类属性，在每个实例中相同

    def __init__(self, name, age, weight):
        self.name = name # 公开属性
        self._age = age # 一般表示私有属性，但是可以在类外直接访问
        self.__weight = weight # 表示私有属性，不能在类外直接访问

    def get_weight(self):
        return self.__weight # 在类中可以访问双下划线实现的私有属性



programmer = Programmer('Albert', 25, 80)
print(dir(programmer))
print(programmer.__dict__)
print(programmer.get_weight())
print(programmer._Programmer__weight)
print(Programmer.hobby)		
		
		"""
if __name__ == '__main__':
    programmer = Programmer('Albert', 25, 80) # 实例化
    print(dir(programmer) # 输出所有属性
    print(programmer.__dict__) # 从构造函数里获得的属性
    print(programmer.get_weight()) # 用双下划线实现的私有属性在类中可以访问
    print(programmer._Programmer__weight) # 但是在类外就需要用这种技巧进行直接访问
    print(Programmer.hobby) # 类属性直接用类名调用，不需要生成对象
"""