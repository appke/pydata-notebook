# coding:utf - 8
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://movie.douban.com/")
bsObj = BeautifulSoup(html, "lxml")  # 将html对象转化为BeautifulSoup对象
liList = bsObj.findAll("li", {"class": "title"})  # 找到所有符合此class属性的li标签
for li in liList:
    name = li.a.get_text()  # 获取标签<a>中文字
    print(name)