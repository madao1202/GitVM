#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/19 10:59
# @Author  : 风暴降生郭德纲
from datetime import datetime

from dingtalkchatbot.chatbot import DingtalkChatbot

current_datetime = datetime.now()
time = current_datetime.strftime('%H:%M')

# WebHook地址
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=a84df00356f9fb088dc8772afafd39638e00f071639f7b0f6dcd1a640948b754'
secret = 'SECf234ad80a95a7ef035c67384b4e1379080e9b193f7849f5548e8975c90be65fa'
# 初始化机器人小丁
xiaoding = DingtalkChatbot(webhook, secret)  # 方式一：通常初始化方式
xiaoding.send_link(title='提醒：%s了！记得点饭！' % time, text='如果不知道点什么看看这个',
                   message_url='https://wndh.net/csm/')
