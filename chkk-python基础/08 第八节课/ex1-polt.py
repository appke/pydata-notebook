
import matplotlib.pyplot as plt  #最好写入到文件中
import numpy as np

a = np.arange(10)
plt.plot(a,a*1.5,a,a*2.5,a,a*3.5,a,a*4.5)
plt.show()