# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 15:11:51 2024

@author: wangzheng3
"""

import time

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"{i}秒后继续……", end="\r")
        time.sleep(1)

if __name__ == "__main__":
    seconds = 3  #设置倒计时时间（秒）
    countdown(seconds)