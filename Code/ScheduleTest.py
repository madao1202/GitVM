# Desc: 定时任务
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/14 17:00
# @Author  : 风暴降生郭德纲
import datetime
import subprocess
import time

import schedule


def job():
    print("运行程序时间", datetime.datetime.now())
    subprocess.run(["python", "VfxPush.py"])


def orderTakeout():
    print("运行程序时间", datetime.datetime.now())
    subprocess.run(["python", "orderTakeout.py"])


def schedule_jobs():
    workdays = [1, 2, 3, 4, 5]
    hours = ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00"]

    for hour in hours:
        schedule.every().day.at(hour).do(job)

    schedule.every().day.at("11:20").do(orderTakeout)

    while True:
        today = datetime.datetime.now().weekday() + 1
        if today in workdays:
            schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    schedule_jobs()
