html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')

#选择元素
print(soup.title)
print(type(soup.title))
print(soup.head)
print(soup.p)  # 输出第一个（匹配第一个）


#获取名称
print(soup.title.name)

#获取属性
print(soup.p.attrs['name'])
print(soup.p['name'])


#获取内容
print(soup.p.string)

#嵌套选择
print(soup.head.title.string)
print(soup.title.string) #title标签唯一

#子节点和子孙节点
print("子节点和子孙节点")
print(soup.p.contents)