import requests
import time
import random
import threading
from bs4 import BeautifulSoup


#读取东方财富网的美股代码
code_US=[]  #8977
name_US=[]
f=open("C:/Users/HL-lisa/Desktop/US.txt","r")
for line in f:
    code=line.split("||")[0]
    code_US.append(code)  
    name_US.append(line.split("||")[1].strip())
f.close()


#协议头和代理
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
https_proxies = [
	{'https':'112.85.171.176:9999'},
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

code=[]
name=[]
logo=[]
company_name=[]
abbr_name=[]
english_name=[]
industry=[]
stock_exchange_name=[]
homepage=[]
people=[]
register_address=[]
address=[]
description=[]


# 奇数
class odd(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		for i in range(1, len(code_US), 2):
			try:
				print("第" + str(i) + "页")
				url = "http://basic.10jqka.com.cn/" + code_US[i] + "/company.html"
				page = requests.get(url, headers=headers, proxies=random.choice(https_proxies)).text
				print("网页长度：" + str(len(page)))
				soup = BeautifulSoup(page)
				table = soup.find("table", attrs={"class": "companyinfo-tab"})
				rows = table.findAll("tr")
				t1 = rows[0].find("img")["src"]  # logo
				t2 = rows[0].findAll("td")[1].text.split("：")[1]  # 公司名称
				t3 = rows[0].findAll("td")[2].text.split("：")[1]  # 公司简称
				t4 = rows[1].findAll("td")[0].text.split("：")[1]  # 英文名称
				t5 = rows[1].findAll("td")[1].text.split("：")[1]  # 所属行业
				t6 = rows[2].find("td").text.split("：")[1]  # 上市场所
				t7 = rows[2].find("a")["href"]  # 公司网址
				t8 = rows[3].findAll("td")[1].text.split("：")[1]  # 注册地址
				t9 = rows[3].findAll("td")[2].text.split("：")[1]  # 员工人数
				t10 = rows[5].find("td").text.split("：")[1]  # 办公地址
				t11 = rows[6].find("td").text.split("：")[1]  # 公司简介
				print(all([t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11]))

				if all([t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11]):
					print("股票代码:" + code_US[i])
					code.append(code_US[i])
					print("股票名称：" + name_US[i])
					name.append(name_US[i])
					print("logo:" + t1)
					logo.append(t1.strip())
					print("公司名称：" + t2)
					company_name.append(t2.strip())
					print("公司简称：" + t3)
					abbr_name.append(t3.strip())
					print("英文名称：" + t4)
					english_name.append(t4.strip())
					print("所属行业：" + t5)
					industry.append(t5.strip())
					print("上市场所：" + t6)
					stock_exchange_name.append(t6.strip())
					print("公司主页：" + t7)
					homepage.append(t7.strip())
					print("注册地址：" + t8)
					people.append(t8.strip())
					print("员工人数：" + t9)
					register_address.append(t9.strip())
					print("办公地址：" + t10)
					address.append(t10.strip())
					print("公司简介：" + t11)
					description.append(t11.strip())
					print("------------------------------------------------")
					time.sleep(3)

				else:
					continue
			except Exception as e:
				print(e)


# 偶数
class even(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		for i in range(0, len(code_US), 2):
			try:
				print("第" + str(i) + "页")
				url = "http://basic.10jqka.com.cn/" + code_US[i] + "/company.html"
				page = requests.get(url, headers=headers, proxies=random.choice(https_proxies)).text
				print("网页长度：" + str(len(page)))
				soup = BeautifulSoup(page)
				table = soup.find("table", attrs={"class": "companyinfo-tab"})
				rows = table.findAll("tr")
				t1 = rows[0].find("img")["src"]  # logo
				t2 = rows[0].findAll("td")[1].text.split("：")[1]  # 公司名称
				t3 = rows[0].findAll("td")[2].text.split("：")[1]  # 公司简称
				t4 = rows[1].findAll("td")[0].text.split("：")[1]  # 英文名称
				t5 = rows[1].findAll("td")[1].text.split("：")[1]  # 所属行业
				t6 = rows[2].find("td").text.split("：")[1]  # 上市场所
				t7 = rows[2].find("a")["href"]  # 公司网址
				t8 = rows[3].findAll("td")[1].text.split("：")[1]  # 注册地址
				t9 = rows[3].findAll("td")[2].text.split("：")[1]  # 员工人数
				t10 = rows[5].find("td").text.split("：")[1]  # 办公地址
				t11 = rows[6].find("td").text.split("：")[1]  # 公司简介
				print(all([t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11]))

				if all([t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11]):
					print("股票代码:" + code_US[i])
					code.append(code_US[i])
					print("股票名称：" + name_US[i])
					name.append(name_US[i])
					print("logo:" + t1)
					logo.append(t1.strip())
					print("公司名称：" + t2)
					company_name.append(t2.strip())
					print("公司简称：" + t3)
					abbr_name.append(t3.strip())
					print("英文名称：" + t4)
					english_name.append(t4.strip())
					print("所属行业：" + t5)
					industry.append(t5.strip())
					print("上市场所：" + t6)
					stock_exchange_name.append(t6.strip())
					print("公司主页：" + t7)
					homepage.append(t7.strip())
					print("注册地址：" + t8)
					people.append(t8.strip())
					print("员工人数：" + t9)
					register_address.append(t9.strip())
					print("办公地址：" + t10)
					address.append(t10.strip())
					print("公司简介：" + t11)
					description.append(t11.strip())
					print("------------------------------------------------")
					time.sleep(3)

				else:
					continue
			except Exception as e:
				print(e)


# 开启进程
us1 = odd()
us1.start()
us2 = even()
us2.start()

import pandas as pd
data={'code':code,'name':name,'logo':logo,'company_name':company_name,'abbr_name':abbr_name,'english_name':english_name,'stock_exchange_name':stock_exchange_name,'industry':industry,'homepage':homepage,'people':people,'register_address':register_address,'address':address,'description':description}
data_US=pd.DataFrame(data)
data_US.to_excel('C:/Users/HL-lisa/Desktop/stock_US_company.xlsx',index=False)
