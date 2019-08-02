#encoding: utf-8

import re

#分组
# text = "apple's price $99,orange's price is $10"
# ret = re.search('.*(\$\d+).*(\$\d+)',text)
# print(ret.group(1))
# print(ret.group(2))
# print(ret.group(1,2))
# #所有的子分组都拿出来
# print(ret.groups())

#findall函数
# text = "apple's price $99,orange's price is $10"
# ret = re.findall('\$\d+',text)
# print(ret)

#findall函数
# text = "apple's price $99,orange's price is $10"
# ret = re.sub('\$\d+','0',text)
# print(ret)


html = """
        <dd class="job_bt">
        <h3 class="description">职位描述：</h3>
        <div class="job-detail">
        <p>岗位职责：</p>
<p>1、负责业务所涉及数据的爬取、清洗、落地、分析。</p>
<p>2、制定并优化爬取策略、爬取调度、爬取解析，解决爬取技术问题，以及确保数据抽取准确。</p>
<p>&nbsp;</p>
<p>任职要求：</p>
<p>1、计算机及相关专业，有网络爬虫研发经验优先。</p>
<p>2、对网络编程，Http协议，Web开发有一定的了解，能熟练使用Python、Java等语言。</p>
<p>3.熟练掌握Python基础知识，熟悉scrapy爬虫框架，有Python实习项目或爬虫经验者优先。</p>
<p>4.有一定JS,CSS基础，熟悉XML,HTML语言和JavaScript等。</p>
<p>5.一定的SQL基础，熟悉主流Mysql，SQL Server等数据库。</p>
<p>6.具有良好的团队合作精神，以及较强的沟通、协调和组织能力；有强烈的责任感和进取心，较强的学习能力</p>
        </div>
    </dd>
"""
# ret = re.sub('<.+?>','',html)
# print(ret)

#split函数
# text = "hello&world ni hao"
# ret = re.split('[^a-zA-Z]',text)
# print(ret)

#compile函数
# text = 'the number is 20.50'
# r = re.compile('\d+\.*\d*')
# ret = re.search(r,text)
# print(ret.group())

text = 'the number is 20.50'
r = re.compile(r"""
    \d+ #小数点前面的数字
    \.? #小数点本身
    \d* #小数点后面的数字
""",re.VERBOSE)
ret = re.search(r,text)
print(ret.group())

