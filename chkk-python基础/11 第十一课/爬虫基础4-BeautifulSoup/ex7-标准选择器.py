'''
find_all( name , attrs , recursive , text , **kwargs )
可根据标签名、属性、内容查找文档
'''

html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')

#name
print('all----------------------------->')
print(soup.find_all('ul'))
print('ul tupy------------------------->')
print(type(soup.find_all('ul')[0]))

#先找到ul，再找li
for ul in soup.find_all('ul'):
    print(ul.find_all('li'))


#attrs
print('属性')
print(soup.find_all(attrs={'id': 'list-1'}))  #字典类型数据
print(soup.find_all(attrs={'name': 'element'}))

#class
print('class')
print(soup.find_all(class_='element')) # 注意class加下划线

#text
print(soup.find_all(text='Foo'))   #返回的是内容

#find_all()   所有的
#find()  返回匹配的第一个