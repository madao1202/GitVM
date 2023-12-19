#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/19 19:12
# @Author  : 风暴降生郭德纲
from selenium import webdriver
from bs4 import BeautifulSoup
import time

def get_google_play_reviews(app_id, num_pages=5):
    base_url = f'https://play.google.com/store/apps/details?id={app_id}&showAllReviews=true'
    all_reviews = []

    # 使用 Chrome 浏览器
    driver = webdriver.Chrome()

    for page in range(1, num_pages + 1):
        url = f'{base_url}&page={page}'
        driver.get(url)

        # 等待页面加载（根据实际情况调整延迟时间）
        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # 查找包含评论的容器
        reviews_container = soup.find('div', class_='VfPpkd-wzTsW')

        # 检查评论容器是否存在
        if reviews_container:
            # 查找单个评论元素
            reviews = reviews_container.find_all('div', class_='RHo1pe')

            for review in reviews:
                # 提取用户、评分和评论
                user = review.find('span', class_='X5PpBb').text
                rating = review.find('div', class_='pf5lIe').find('div')['aria-label']
                comment = review.find('span', jsname='h3YV2d').text

                # 将评论添加到列表
                all_reviews.append({'User': user, 'Rating': rating, 'Comment': comment})

        else:
            print(f'在第 {page} 页未找到评论容器')

    driver.quit()  # 关闭浏览器
    return all_reviews

if __name__ == "__main__":
    app_id = "com.HoYoverse.hkrpgoversea"
    reviews = get_google_play_reviews(app_id, num_pages=3)

    # 打印所有评论
    for review in reviews:
        print(f'用户: {review["User"]}\n评分: {review["Rating"]}\n评论: {review["Comment"]}\n{"-"*30}')
