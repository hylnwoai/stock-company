from lxml import etree
import requests
import time
import random

#读取东方财富网的港股代码
code_HK=[]
name_HK=[]
f=open("C:/Users/HL-lisa/Desktop/HK.txt","r")
for line in f:
    code=line.split("||")[0]
    code_HK.append("HK"+code[1:])  #将港股代码转化成符合同花顺的格式
    name_HK.append(line.split("||")[1].strip())
f.close()

#协议头和代理
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
https_proxies = [
    {'https':'120.83.108.181:9999'},
    {'https':'125.110.75.200:8118'},
    {'https':'120.83.105.15:9999'},
      {'https':'123.163.97.238:9999'},
    {'https':'120.83.97.131:9999'}
]
http_proxies = [
    {'http':'222.189.190.200:9999'},
    {'http':'117.91.133.226:9999'},
    {'http':'117.91.133.226:9999'}
]

#存储各字段信息的列表
company_name=[]
industry=[]
people=[]
register_address=[]
address=[]
homepage=[]
business=[]
description=[]

code=[]
name=[]


for i in range(len(code_HK)):
    try:
        print("第" + str(i) + "页")
        url = "http://stockpage.10jqka.com.cn/" + code_HK[i] + "/company"

        page = requests.get(url=url, headers=headers, proxies=random.choice(https_proxies)).text
        print("网页长度："+str(len(page)))

        response = etree.HTML(page)  # 网页内容

        t1 = response.xpath('//*[@id="basic"]/div[2]/table/tbody/tr[1]/td[1]/span')[0].text  #公司名称
        t2 = response.xpath('//*[@id="basic"]/div[2]/table/tbody/tr[1]/td[2]/span')[0].text  #所属行业
        t3 = response.xpath('//*[@id="basic"]/div[2]/table/tbody/tr[3]/td[1]/span')[0].text  #员工人数
        t4 = response.xpath('//*[@id="basic"]/div[2]/table/tbody/tr[4]/td[1]/span/a')[0].text  #注册地址
        t5 = response.xpath('//*[@id="basic"]/div[2]/table/tbody/tr[4]/td[2]/span/a')[0].text  #公司地址
        t6 = response.xpath('//*[@id="basic"]/div[2]/table/tbody/tr[6]/td[1]/span/a')[0].text   #主页
        t7 = response.xpath('//*[@id="basic"]/div[2]/table/tbody/tr[8]/td/span')[0].text  #主营业务
        t8 = response.xpath('//*[@id="introduce"]/div[2]/div/p/text()')[0]  #公司简介
        print(all([t1,t2,t3,t4,t5,t6,t7,t8]))

        if  all([t1,t2,t3,t4,t5,t6,t7,t8]):  #避免部分字段时为空，导致最后各字段的长度不一致
            print("股票代码:" + code_HK[i])
            code.append(code_HK[i])
            print("股票名称：" + name_HK[i])
            name.append(name_HK[i])
            print("公司名称：" + t1)
            company_name.append(t1.strip())
            print("所属行业：" + t2)
            industry.append(t2.strip())
            print("员工人数：" + t3)
            people.append(t3.strip())
            print("注册地址：" + t4)
            register_address.append(t4.strip())
            print("公司总部：" + t5)
            address.append(t5.strip())
            print("公司主页：" + t6)
            homepage.append(t6.strip())
            print("主营业务：" + t7)
            business.append(t7.strip())
            print("公司简介：" + t8)
            description.append(t8.strip())

            print("------------------------------------------------")
            time.sleep(3)
        else:
            continue
    except Exception as e:
        print(e)


import pandas as pd
data={'code':code,'name':name,'company_name':company_name,'industry':industry,'people':people,'register_address':register_address,'address':address,'homepage':homepage,'business':business,'description':description}
data_HK=pd.DataFrame(data)
