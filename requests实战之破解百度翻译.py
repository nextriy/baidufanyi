#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2022/12/31 0031 16:43
# @Author  : captain
# @Email   : 2067266431@qq.com
# @File    : 02.requests实战之破解百度翻译.py
# @Software: PyCharm

import requests
import json

if __name__=="__main__":
    # 1.指定url
    url = "https://fanyi.baidu.com/sug"
    # 2.UA伪装
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }
    key = input("请输入要翻译的关键词：")
    data={
        "kw": key
    }
    # 3.发送请求
    try:
        response = requests.post(url=url,data=data,headers=headers).json()
        response = response['data'][0]['k']+"对应的翻译是："+response['data'][0]['v']
        print(response)

    except:
        print("您输入的关键字有误!")


    # 4.持久化存储
    fp = open("./翻译结果.json",'w',encoding='utf-8')
    json.dump(response,fp=fp,ensure_ascii=False)
    print("over!!!")