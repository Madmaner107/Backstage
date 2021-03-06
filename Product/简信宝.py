#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/1/10 0010 11:18 
# @Author : Chihiro 
# @Site :  
# @File : 简信宝.py 
# @Software: PyCharm




from requests import Session
from BaseSpider import BaseSpider
from DealWithCookie import cookie_to_dict
from scrapy import Selector
from time import sleep
import time

class XHY(BaseSpider):
    def __init__(self, account):
        super(XHY, self).__init__(account)

    def get_info(self):

        # 设置session
        session = Session()
        # 设置头部信息
        headers = {
            "Cookie": "PHPSESSID=76bcb2dcbc3c8222df29786dd1095da7; XSRF-TOKEN=eyJpdiI6ImQzVlwvb2RcL01jMXNrRkZoeU1wSzRWZz09IiwidmFsdWUiOiJCM1dpTU52SHc2UlFoRlJ4WStiSFpIZEplUHlJT3pzNmIzK3dGR0l5amNVejBwcUxnMjJ5NlN5K2dxbHdGOXJXbFdjcVQreENoemNYQVZZRlhFR091UT09IiwibWFjIjoiZDNhNTFmN2RkNWYzNTc3MTQ3ZGQ2ZmU5ZmUyZGQ1MDAzMmMxZWMxNDliMWVkNDFjM2Y2MDdhZjRiMTFhMGZkZCJ9; laravel_session=eyJpdiI6IjhYdUdDb1wvUFgrOEdVd1laaWtrczV3PT0iLCJ2YWx1ZSI6Ilo5cEw0MndMMzJHak1wNStTa0luZmtnXC9sMVNLeUI5U0Z6MzJqK0c1Qkx4b0tjcE9XQlwvWmtcL1FIMEtvVnFDeVM1cXZrSWhIYW5sRmw0OWVaS2cxb1lBPT0iLCJtYWMiOiJmNmJhZTFiMWQyMWI0ZmQyMzUyOTdmZTJmMmVjZGZhNGY3N2Q0YzE2MTI5YjA4ZTUxYjJjZTM0YTQ4M2Q3YjQ3In0%3D",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
        }
        # 页面url
        url = 'http://www.daohuixinxi.com/admin/promoter/user'
        #参数

        # 请求url
        response = session.get(url, headers=headers)
        # 构造Selector
        info = Selector(text=response.text)
        num = info.xpath('/html/body/div/div[1]/div[1]/div/font[2]/text()').extract()[0]
        # 获取结果
        result = {
            "注册人数": num,
            "实名人数": "null",
            "申请人数": "null",
            "放款人数": "null"
        }
        self.write_sql(result)
        print(result)


WD = {
    "login_url": "",
    "area": "",
    "product": "",
    "username": "",
    "password": "",
    "channel": ""
}


all_area = [WD]


for each in all_area:
    XHY(each).get_info()
    sleep(1200)


