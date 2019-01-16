# _*_ coding: utf-8 _*_

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#
# Author: yz
# Date: 2017-12-3
#
'''
增加子图 add_subplot(first,second,index)
指定图像大小 plt.figure(figsize=(12, 6)) 
指定线条的颜色 plt.plot(unrate[0:12]["MONTH"], unrate[0:12]["VALUE"], c="red")
添加标签并指定位置 plt.plot(subset["MONTH"], subset["VALUE"], c=colors[i], label=label) plt.legend(loc='upper left')
'''


'''
add_subplot(first,second,index) first means number of Row,second means number of Column.
'''
# fig = plt.figure()
# ax1 = fig.add_subplot(3, 2, 1)
# ax2 = fig.add_subplot(3, 2, 2)
# ax3 = fig.add_subplot(3, 2, 3)
# ax6 = fig.add_subplot(3, 2, 6)
# ax1.plot(np.random.randint(1, 5, 5), np.arange(5))
# ax2.plot(np.arange(10) * 3, np.arange(10))
# plt.show()


'''
指定颜色和大小
'''
unrate = pd.read_csv("data/UNRATE.csv")
unrate["DATE"] = pd.to_datetime(unrate["DATE"])
unrate["MONTH"] = unrate["DATE"].dt.month

# fig = plt.figure(figsize=(12, 6))   # figsize 图像大小
# plt.plot(unrate[0:12]["MONTH"], unrate[0:12]["VALUE"], c="red") # c 指定线条颜色
# plt.plot(unrate[12:24]["MONTH"], unrate[12:24]["VALUE"], c="green")
# plt.show()


'''
lable
'''
fig = plt.figure(figsize=(10, 6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i * 12
    end_index = (i + 1) * 12
    label = str(1948 + i)
    subset = unrate[start_index:end_index]
    plt.plot(subset["MONTH"], subset["VALUE"], c=colors[i], label=label)    # 添加lable
# 指定lable的位置 'best' 'upper right/left'  'lower right/left' 'right' 'center right/left' 'upper/lower center' 'center'
plt.legend(loc='upper left')
# print(help(plt.legend))
plt.xlabel('Month, Integer')
plt.ylabel('Unemployment Rate, Percent')
plt.title('Monthly Unemployment Trends, 1948-1952')
plt.show()
