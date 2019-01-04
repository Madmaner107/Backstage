# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018年12月26日 22:17
# @Author  : 逗比i
# @Project : Backstage
# @File    : 点容宝.py
# @Software: PyCharm
# @Describe:

from requests import Session
from BaseSpider import BaseSpider
from DealWithCookie import cookie_to_dict
from scrapy import Selector
from time import sleep
import json
import time


class DRB(BaseSpider):
    def __init__(self, account):
        super(DRB, self).__init__(account)


    def get_info(self):
        xpath_info = {
            "username": '//*[@id="app"]/div/div/div[2]/form/div[1]/div/div/input',
            "password": '//*[@id="app"]/div/div/div[2]/form/div[2]/div/div/input',
            "login_button": '//*[@id="app"]/div/div/div[2]/form/div[3]/button',
            "check_code": '',
            "code_image_url": '',
            "success_ele": ''
        }
        # 获取cookie
        token = self.no_check_get_token(xpath_info, 'cms_web_token')
        # 将cookie设置给session
        # 设置session
        session = Session()
        # 设置头部信息
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
            'Host': 'merchant.xianjinxia.com',
            'loginToken': token,
            'Origin': 'http: // merchant.xianjinxia.com',
            'Referer': 'http: // merchant.xianjinxia.com /'
        }
        # 页面url
        json_url = "http://merchant.xianjinxia.com/api/v2/merchant/admin/youmi/statisticsThirdPage"
        args = {
            'channelName': f"{self.channel}",
            'dtEnd': int(time.mktime(time.strptime(f"{self.today} 00:00:00", "%Y-%m-%d %H:%M:%S"))) * 1000,
            'dtStart': int(time.mktime(time.strptime(f"{self.today} 00:00:00", "%Y-%m-%d %H:%M:%S"))) * 1000,
            'dtRange': [int(time.mktime(time.strptime(f"{self.today} 00:00:00", "%Y-%m-%d %H:%M:%S"))) * 1000,
                        int(time.mktime(time.strptime(f"{self.today} 00:00:00", "%Y-%m-%d %H:%M:%S"))) * 1000, ]
        }
        # 请求url
        response = session.post(json_url, headers=headers, json=args)
        info = response.json()
        print(info)
        # info = response.json()['data']['pageInfo']['list'][0]

        info = response.json()['data']['list'][0]
        # 获取结果
        result = {
            "注册人数": info['regCount'],
            "实名人数": "null",
            "申请人数": 'null',
            "放款人数": 'null'
        }
        self.write_sql(result)


WD = {
    "login_url": 'http://merchant.xianjinxia.com/#/login',
    "area": "外地",
    "product": "有米管家",
    "username": "13685746960",
    "password": "13685746960",
    "channel": "ymgj-yfwk1"
}

SP = {
    "login_url": 'http://merchant.xianjinxia.com/#/login',
    "area": "四平",
    "product": "有米管家",
    "username": "13685746960",
    "password": "13685746960",
    "channel": "有米管家-悦富万卡"
}






all_area = [WD, SP]

while True:
    for each in all_area:
        DRB(each).get_info()
    sleep(600)













