#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/13 11:29
# @Author  : 风暴降生郭德纲
from datetime import datetime

from dingtalkchatbot.chatbot import DingtalkChatbot

current_datetime = datetime.now()
time = current_datetime.strftime('%H:%M')

# WebHook地址
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=c99bc7184ca9f2296bf6b027364e49af5cc1f65936f5d068db4151ded260c329'
secret = 'SEC1d42cf1b9a6563559766790811441680a34b9cda0ecfdb24a77c51a9eb694d36'
# 初始化机器人小丁
xiaoding = DingtalkChatbot(webhook, secret)  # 方式一：通常初始化方式
# Link消息
xiaoding.send_link(title='提醒：%s了！记得点饭！' % time, text='如果不知道点什么看看这个',
                   message_url='https://wndh.net/csm/')
