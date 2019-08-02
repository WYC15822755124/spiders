import requests
import re

def main() :
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
    }
    url = "https://www.qq.com"
    response = requests.get(url,headers=headers)
    text = response.text
    # with open('qq.html','w',encoding='utf-8') as fp:
    #     fp.write(text)
    print(text)

if __name__ == '__main__':
    main()