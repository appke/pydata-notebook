#-*- coding: utf-8 -*-
import re
import csv
import requests
from tqdm import tqdm
from urllib.parse import urlencode
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

def get_detail_page(url):
    '''
    获取职位详情页html内容并返回
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Host': 'jobs.zhaopin.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }

    try:
        # 获取网页内容，返回html数据
        response = requests.get(url, headers=headers)
        # 通过状态码判断是否获取成功
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:
        return None

#进阶版不用这个函数了
def get_one_page(city, keyword, region, page):
    '''
    获取网页html内容并返回
    '''
    # 构造请求地址
    paras = {
        'jl': city,         # 搜索城市
        'kw': keyword,      # 搜索关键词
        'isadv': 0,         # 是否打开更详细搜索选项
        'isfilter': 1,      # 是否对结果过滤
        'p': page,          # 页数
        're': region        # region的缩写，地区，2005代表海淀
    }
    #请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Host': 'sou.zhaopin.com',
        'Referer': 'https://www.zhaopin.com/',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }

    #url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?' + urlencode(paras)
    #用reuqests库可以完成此工作
    url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?'
    try:
        # 获取网页内容，返回html数据
        #response = requests.get(url, headers=headers)
        response = requests.get(url, params=paras, headers=headers)
        # 通过状态码判断是否获取成功
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:
        return None

def parse_one_page(html):
    '''
    解析HTML代码，提取有用信息并返回
    '''
    # 正则表达式进行解析：岗位名称/公司名称/公司详细地址/薪资
    # pattern = re.compile('<a style=.*? target="_blank">(.*?)</a>.*?'        # 匹配职位信息
    #     '<td class="gsmc"><a href="(.*?)" target="_blank">(.*?)</a>.*?'     # 匹配公司网址和公司名称
    #     '<td class="zwyx">(.*?)</td>', re.S)                                # 匹配月薪

    #修改正则表达式，获取更详细的信息
    pattern = re.compile('<td class="zwmc".*?href="(.*?)" target="_blank">(.*?)</a>.*?'  # 匹配职位详情地址和职位名称
                         '<td class="gsmc">.*? target="_blank">(.*?)</a>.*?'  # 匹配公司名称
                         '<td class="zwyx">(.*?)</td>', re.S)  # 匹配月薪

    # 匹配所有符合条件的内容
    items = re.findall(pattern, html)

    #在解析之后要对该数据进行处理剔除标签
    for item in items:
        job_name = item[0]
        job_name = job_name.replace('<b>', '')
        job_name = job_name.replace('</b>', '')

        salary_avarage = 0
        temp = item[3]
        if temp != '面议':
            idx = temp.find('-')
            # 求平均工资
            salary_avarage = (int(temp[0:idx]) + int(temp[idx+1:]))//2

        yield {
            'job': job_name,
            'website': item[1],
            'company': item[2],
            'salary': item[3]
        }

def write_csv_file(path, headers, rows):
    '''
    将表头和行写入csv文件
    '''
    # 加入encoding防止中文写入报错
    # newline参数防止每写入一行都多一个空行
    with open(path, 'a', encoding='gb18030', newline='') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(rows)

def write_csv_headers(path, headers):
    '''
    写入表头
    '''
    with open(path, 'a', encoding='gb18030', newline='') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()

def write_csv_rows(path, headers, rows):
    '''
    写入行
    '''
    with open(path, 'a', encoding='gb18030', newline='') as f:
        f_csv = csv.DictWriter(f, headers)
        # 如果写入数据为字典，则写入一行，否则写入多行
        if type(rows) == type({}):
            f_csv.writerow(rows)
        else:
            f_csv.writerows(rows)

def write_txt_file(path, txt):
    '''
    写入txt文本
    '''
    with open(path, 'a', encoding='gb18030', newline='') as f:
        f.write(txt)

def get_job_detail(html):
    requirement = ''
    # 使用BeautifulSoup进行数据筛选\
    # print(html) why none
    soup = BeautifulSoup(html, 'html.parser')
    # 找到<ul class="terminal-ul clearfix">标签
    for ul in soup.find_all('ul', class_='terminal-ul clearfix'):
        # 该标签共有8个子标签，分别为：
        # 职位月薪|工作地点|发布日期|工作性质|工作经验|最低学历|招聘人数|职位类别
        lis = ul.find_all('strong')
        # 工作经验
        years = lis[4].get_text()
        # 最低学历
        education = lis[5].get_text()
    # 筛选任职要求
    for terminalpage in soup.find_all('div', class_='terminalpage-main clearfix'):
        for box in terminalpage.find_all('div', class_='tab-cont-box'):
            cont = box.find_all('div', class_='tab-inner-cont')[0]
            ps = cont.find_all('p')
            # "立即申请"按钮也是个p标签，将其排除
            for i in range(len(ps) - 1):
                requirement += ps[i].get_text().replace("\n", "").strip()   # 去掉换行符和空格

    # 筛选公司规模，该标签内有四个或五个<li>标签，但是第一个就是公司规模
    scale = soup.find(class_='terminal-ul clearfix terminal-company mt20').find_all('li')[0].strong.get_text()

    return {'years': years, 'education': education, 'requirement': requirement, 'scale': scale}


def main(city, keyword, region, pages):
    '''
    主函数
    '''
    csv_filename = 'zl_' + city + '_' + keyword + '.csv'
    txt_filename = 'zl_' + city + '_' + keyword + '.txt'
    headers = ['job', 'years', 'education', 'salary', 'company', 'scale', 'job_url']
    write_csv_headers(csv_filename, headers)
    for i in range(pages):
        '''
        获取该页中所有职位信息，写入csv文件
        '''
        job_dict = {}
        html = get_one_page(city, keyword, region, i)
        #if html == None:
        #    continue
        items = parse_one_page(html)
        for item in items:
            #print(html)
            html = get_detail_page(item.get('job_url'))

            job_detail = get_job_detail(html)

            job_dict['job'] = item.get('job')
            job_dict['years'] = job_detail.get('years')
            job_dict['education'] = job_detail.get('education')
            job_dict['salary'] = item.get('salary')
            job_dict['company'] = item.get('company')
            job_dict['scale'] = job_detail.get('scale')
            job_dict['job_url'] = item.get('job_url')

            # 对数据进行清洗，将标点符号等对词频统计造成影响的因素剔除
            pattern = re.compile(r'[一-龥]+')
            filterdata = re.findall(pattern, job_detail.get('requirement'))
            write_txt_file(txt_filename, ''.join(filterdata))
            write_csv_rows(csv_filename, headers, job_dict)

if __name__ == '__main__':
    main('北京', 'python工程师', 2005, 10)