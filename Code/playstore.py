#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/21 17:36
# @Author  : 风暴降生郭德纲
from DrissionPage import WebPage
from DrissionPage import ChromiumOptions
from DrissionPage import SessionOptions
from DrissionPage.common import Settings
from DrissionPage.common import Keys
from DrissionPage.common import wait_until
from DrissionPage.common import make_session_ele
from DrissionPage.common import configs_to_here
from DrissionPage import ChromiumPage

# Creating page object
page = ChromiumPage()

# App ID
APP_ID = 'com.metroville.global'

# Controlling the browser to visit play.google.com
page.get(f'https://play.google.com/store/apps/details?id={APP_ID}')  # Using the page object to visit
#
# # Clicking the "More Ratings" button
# page.ele('#ow286 > section > header > div > div:nth-child(2) > button').click()
