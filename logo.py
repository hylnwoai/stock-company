# 去掉抓取下来的默认图片default.png

import requests
import time
import random

#读取美英股票上市公司的logo  #7080
logo=[]
f=open("C:/Users/HL-lisa/Desktop/logo.txt","r")
for line in f:
    logo.append(line.strip())
f.close()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
https_proxies = [
    {'https':'120.83.108.181:9999'},
    {'https':'125.110.75.200:8118'},
    {'https':'120.83.105.15:9999'},
      {'https':'123.163.97.238:9999'},
    {'https':'120.83.97.131:9999'}
]

default=requests.get("http://eq.10jqka.com.cn/logo/default.png",headers=headers)
n=len(default.text)   #默认页面长度230


useful_logo=[]
for i in range(len(logo)):
    try:
        url=logo[i]
        page=requests.get(url=url,headers=headers, proxies=random.choice(https_proxies))
        print("第"+str(i)+"页："+str(len(page.text)))
        if len(page.text)<300:
            useful_logo.append("")
        else:
            useful_logo.append(logo[i])
        time.sleep(1)
    except Exception as e:
        print(e)
