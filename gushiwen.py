import requests
import re

def parse_page(url) :
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    text = response.text
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>',text,re.DOTALL)  #re.DOTALL可以匹配所有字符 \n
    dynasties = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    authors = re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    content_tag = re.findall(r'<div class="contson" .*?>(.*?)</div>',text,re.DOTALL)
    contents = []
    for content in content_tag :
        x = re.sub(r'<.*?>','',content)
        contents.append(x.strip())
    poems = []
    for value in zip(titles,dynasties,authors,contents) :
        titles,dynasties,authors,contents = value
        poem = {
            'title':titles,
            'dynasties':dynasties,
            'authors':authors,
            'contents':contents
        }
        poems.append(poem)
    for poem in poems :
        print(poem)
        print('='*40)

def main() :
    # url = 'https://www.gushiwen.org/default_1.aspx'
    for x in range(1,101) :
        url = 'https://www.gushiwen.org/default_%s.aspx' % x
        parse_page(url)

if __name__ == '__main__':
    main()