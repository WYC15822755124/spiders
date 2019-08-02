#encoding: utf-8

import requests
import re
import json
import pymysql
duanziS = []
conn = pymysql.connect(host='localhost', user='root', password='621121', database='pymysql_demo', port=3306)
cursor = conn.cursor()

def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    text = response.text
    # authors = re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    authors = re.findall(r'<div class="author clearfix">.*?<a.*?alt="(.*?)">',text,re.DOTALL)
    content_tag = re.findall(r'<div class="content">.*?<span>(.*?)</span>',text,re.DOTALL)
    contents = []
    for content in content_tag :
        content = re.sub(r'[\n<br/>]', '', content)
        contents.append(content.strip())

    for value in zip(authors,contents):
        author,content = value
        duanzi = {
            'author':author,
            'content':content
        }
        duanziS.append(duanzi)



    # with open('duanzi.txt','w') as fp:
    #     fp.write(duanziS)




def main():
    # url = "https://www.qiushibaike.com/text/page/1/"
    for x in range(1,14) :
        url = 'https://www.qiushibaike.com/text/page/ %s /'%(x)
        parse_page(url)

    #以字符串写入文档
    # duanziStr = str(duanziS)
    # with open('duanzi.txt','w', encoding='utf-8') as fp:
    #     fp.write(duanziStr)

    #写入json
    # json_str = json.dumps(duanziS)
    # print(json_str)
    # with open('duanzi.json','w',encoding='utf-8') as fp:
    #     # fp.write(json_str)
    #     json.dump(duanziS,fp,ensure_ascii=False)

    for duanzi in duanziS:
        author = duanzi['author']
        content = duanzi['content']

        sql = """
            insert into duanzi (author,content) values (%s,%s) 
        """
        cursor.execute(sql, (author,content))
        conn.commit()
    conn.close()



if __name__ == '__main__':
    main()