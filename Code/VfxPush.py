#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/13 12:55
# @Author  : 风暴降生郭德纲
import json

import requests
from bs4 import BeautifulSoup
from dingtalkchatbot.chatbot import DingtalkChatbot

# WebHook地址
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=a84df00356f9fb088dc8772afafd39638e00f071639f7b0f6dcd1a640948b754'
secret = 'SECf234ad80a95a7ef035c67384b4e1379080e9b193f7849f5548e8975c90be65fa'
# 初始化机器人小丁
xiaoding = DingtalkChatbot(webhook, secret)  # 方式一：通常初始化方式


def get_weather():
    url = "http://www.weather.com.cn/weather/101210101.shtml"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    weather = soup.find("p", class_="wea").get_text()
    temperature = soup.find("p", class_="tem").get_text().replace("\n", "")
    return weather, temperature


# 每日一言示例对接
url = 'https://v.api.aa1.cn/api/api-wenan-anwei/index.php?type=json'
response = requests.get(url)
res = json.loads(response.text)
text = res['anwei']
# 摸鱼日报示例对接
url = 'https://dayu.qqsuu.cn/moyuribao/apis.php?type=json'
response = requests.get(url)
res = response.json()
# 当前时间示例
from datetime import datetime

current_datetime = datetime.now()
time = current_datetime.strftime('%H:%M:%S')
if __name__ == "__main__":
    weather, temperature = get_weather()
    # Text消息@所有人
    xiaoding.send_text(msg=f"杭州天气: {weather}, 温度: {temperature}\n 每日随机一句屁话:{text}\n {time}了，该提肛了",
                       is_at_all=False)
    # xiaoding.send_image(pic_url=res.get('data', 'No data found'))
