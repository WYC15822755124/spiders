#encoding: utf-8
#港澳台不能正常显示 table标签不完整 要用html5lib

import requests
from bs4 import BeautifulSoup
from pyecharts import Bar
import time

TIME = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
ALL_DATA = []

def parse_page(url):
    headers = {
        'User-Agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text,'html5lib')
    conMidtab = soup.find('div',class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index,tr in enumerate(trs):
            tds = tr.find_all('td')
            city_td = tds[0]
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]
            ALL_DATA.append({"city":city,"min_temp":int(min_temp)})
            # print({"city":city,"min_temp":int(min_temp)})


def main():
    # url = 'http://www.weather.com.cn/textFC/gat.shtml'
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml'
    ]
    for url in urls :
        parse_page(url)

    #分析数据
    #根据最低气温进行排序
    # def sorr_key (data) :
    #     min_temp = data['min_temp']
    #     return min_temp
    ALL_DATA.sort(key=lambda data:data['min_temp'])
    # print(ALL_DATA[0:10])
    data = ALL_DATA[0:20]

    # cities = []
    # for city_temp in data:
    #     city = city_temp['city']
    #     cities.append(city)


    cities = list(map(lambda x:x['city'],data))
    temps = list(map(lambda x:x['min_temp'],data))
    #pyecharts
    chart = Bar("中国天气最低气温排行榜")
    chart.add('',cities,temps)
    chart.render(TIME+'temperature.html')



if __name__ == '__main__':
    main()




















