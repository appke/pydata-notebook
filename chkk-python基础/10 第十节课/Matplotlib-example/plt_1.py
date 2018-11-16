# _*_ coding: utf-8 _*_

import pandas as pd
import matplotlib.pyplot as plt

#
# Author: yz
# Date: 2017-12-3
#

'''
pandas导入数据和date格式转换
matplotlib基本的绘图：横纵坐标标签，标题，坐标值旋转等
'''


# 导入数据
unrate = pd.read_csv("data/UNRATE.csv")
unrate["DATE"] = pd.to_datetime(unrate["DATE"])  # 1948/1/1 -> 1948-01-01
# print(unrate.head(10))
'''
        DATE  VALUE
0 1948-01-01    3.4
1 1948-02-01    3.8
2 1948-03-01    4.0
3 1948-04-01    3.9
4 1948-05-01    3.5
5 1948-06-01    3.6
6 1948-07-01    3.6
7 1948-08-01    3.9
8 1948-09-01    3.8
9 1948-10-01    3.7
'''

# plt.plot()
# plt.show()

'''
While the y-axis looks fine, the x-axis tick labels are too close together and are unreadable
We can rotate the x-axis tick labels by 90 degrees so they don't overlap
We can specify degrees of rotation using a float or integer value.
'''
# first_twelve = unrate[0:12]
# plt.plot(first_twelve["DATE"], first_twelve["VALUE"])
# plt.xticks(rotation=45) # x坐标值太长时，可以让其旋转再显示
# # print(help(plt.xticks))
# plt.show()


'''
xlabel(): accepts a string value, which gets set as the x-axis label.
ylabel(): accepts a string value, which is set as the y-axis label.
title(): accepts a string value, which is set as the plot title.
'''
first_twelve = unrate[0:12]
plt.plot(first_twelve['DATE'], first_twelve['VALUE'])
plt.xticks(rotation=45)
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends, 1948')
plt.show()