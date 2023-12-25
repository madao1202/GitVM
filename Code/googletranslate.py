#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/25 11:30
# @Author  : 风暴降生郭德纲
from googletrans import Translator
translator = Translator()

languages = ['zh-cn','en','es','pt','id','zh-tw','de','fr','it','ja','ko','ru','th','tr','vi','ar']
language_names = {
    'zh-cn': '汉语',
    'en': '英语',
    'es': '西班牙语',
    'pt': '葡萄牙语',
    'id': '印度尼西亚语',
    'zh-tw': '繁体中文',
    'de': '德语',
    'fr': '法语',
    'it': '意大利语',
    'ja': '日语',
    'ko': '韩语',
    'ru': '俄语',
    'th': '泰语',
    'tr': '土耳其语',
    'vi': '越南语',
    'ar': '阿拉伯语'
}

while True:
    text = input('请输入要翻译的内容，或者输入"quit"退出程序：')
    if text.lower() == 'quit':
        break
    out=[]
    for lang in languages:
        translation = translator.translate(text, dest=lang).text
        print(f"{language_names[lang]}--{translation}")
        out.append(translation)
    print('------------复制至表格中---------------')
    for _ in out:
        print(_,end='\n')
    print('------------翻译已完成---------------')



