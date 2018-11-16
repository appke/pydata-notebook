# coding:utf - 8
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://tieba.baidu.com/")
bsObj = BeautifulSoup(html, "lxml")  # 将html对象转化为BeautifulSoup对象
# BeautifulSoup将html对象进行了层次化处理了，
# 对它的原网页的标签进行了逐层的处理和细化，以便于我们之后使用
print(bsObj.title)  # 输出这个网页中的标题  title+标题内容
print(bsObj.title.string)  # 标题内容
print(bsObj.title.name)    # 标签名称