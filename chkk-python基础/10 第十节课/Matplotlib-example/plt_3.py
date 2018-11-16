# _*_ coding: utf-8 _*_

import pandas as pd
import matplotlib.pyplot as plt
from numpy import arange

#
# Author: yz
# Date: 2017-12-3
#

'''
柱状图 fig, ax = plt.subplots()  ax.bar(bar_positions, bar_heights, 0.5)
散点图
'''

#
# 导入数据
#
reviews = pd.read_csv("data/fandango_scores.csv")
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
norm_reviews = reviews[cols]
# print(norm_reviews[:1])

#
# 柱状图
#
# num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
# bar_heights = norm_reviews.ix[0, num_cols].values
# # print(bar_heights)  # [4.2999999999999998 3.5499999999999998 3.8999999999999999 4.5 5.0]
# bar_positions = arange(5) + 0.75
# # print(bar_positions)    # [1 2 3 4 5]
# fig, ax = plt.subplots()
# ax.bar(bar_positions, bar_heights, 0.5)
# plt.show()

#
# 将坐标值改为标签 ax.set_xticklabels(num_cols, rotation=45)
#
# num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
# bar_heights = norm_reviews.ix[0, num_cols].values
# # print(bar_heights)  # [4.2999999999999998 3.5499999999999998 3.8999999999999999 4.5 5.0]
# bar_positions = arange(5) + 0.75
# # print(bar_positions)    # [1 2 3 4 5]
# fig, ax = plt.subplots()
# ax.bar(bar_positions, bar_heights, 0.5)
#
# tick_positions = range(1,6)
# ax.set_xticks(tick_positions)
# ax.set_xticklabels(num_cols, rotation=45)
#
# ax.set_xlabel('Rating Source')
# ax.set_ylabel('Average Rating')
# ax.set_title('Average User Rating For Avengers: Age of Ultron (2015)')
# plt.show()

# fig, ax = plt.subplots()
# # ax.hist(norm_reviews['Fandango_Ratingvalue'])
# # ax.hist(norm_reviews['Fandango_Ratingvalue'],bins=20)
# ax.hist(norm_reviews['Fandango_Ratingvalue'], range=(3, 5),bins=20)
# plt.show()


#
# 散点图
#
fig, ax = plt.subplots()
ax.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])
# ax.scatter([4.5, 3], [4.3, 4])    # （4.5， 4.3） （3， 4）
ax.set_xlabel('Fandango')
ax.set_ylabel('Rotten Tomatoes')
plt.show()
