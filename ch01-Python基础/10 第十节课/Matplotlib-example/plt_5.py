# _*_ coding: utf-8 _*_

import pandas as pd
import matplotlib.pyplot as plt

#
# Author: yz
# Date: 2017-12-3
#

'''
线的颜色和状态
'''

women_degrees = pd.read_csv('data/percent-bachelors-degrees-women-usa.csv')
major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']


# cb_dark_blue = (0/255, 107/255, 164/255)
# cb_orange = (255/255, 128/255, 14/255)
#
# fig = plt.figure(figsize=(12, 12))
#
# for sp in range(0,4):
#     ax = fig.add_subplot(2,2,sp+1)
#     # The color for each line is assigned here.
#     ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c=cb_dark_blue, label='Women')
#     ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c=cb_orange, label='Men')
#     for key,spine in ax.spines.items():
#         spine.set_visible(False)
#     ax.set_xlim(1968, 2011)
#     ax.set_ylim(0,100)
#     ax.set_title(major_cats[sp])
#     ax.tick_params(bottom="off", top="off", left="off", right="off")
#
# plt.legend(loc='upper right')
# plt.show()


#Setting Line Width
cb_dark_blue = (0/255, 107/255, 164/255)
cb_orange = (255/255, 128/255, 14/255)

fig = plt.figure(figsize=(12, 12))

for sp in range(0,4):
    ax = fig.add_subplot(2,2,sp+1)
    # Set the line width when specifying how each line should look.
    ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c=cb_dark_blue, label='Women', linewidth=10)
    ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c=cb_orange, label='Men', linewidth=10)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(major_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")

plt.legend(loc='upper right')
plt.show()