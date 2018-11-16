
#
#通过select()直接传入CSS选择器即可完成选择

html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
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
print(soup.select('.panel .panel-heading'))  #如果是class，则在前面加点.
print(soup.select('ul li'))                 #如果是标签
print(soup.select('#list-2 .element'))      #如果是id，这在前面加#
            #查找 id=list-2   下，class=element的标签
print(type(soup.select('ul')[0]))

#层层 嵌套选择
for ul in soup.select('ul'):
    print(ul.select('li'))


#获取属性
for ul in soup.select('ul'):
    print(ul['id'])        #两种方法均可
    print(ul.attrs['id'])   #输出id属性

#获取内容
for li in soup.select('li'):
    print(li.get_text())