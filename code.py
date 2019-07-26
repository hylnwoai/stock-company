import urllib.request
import re
import urllib.error
import time
import threading

#模拟浏览器
headers=("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)

'''
url="http://97.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124002685751742868736_1563960115304&pn=3&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:105,m:106,m:107&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152"
page=urllib.request.urlopen(url).read().decode("utf-8","ignore")
print(len(page))

pat1='"f12":"(.*?)"'  #代码
pat2='"f14":"(.*?)"'  #名称

res1=re.compile(pat1).findall(page)
res2=re.compile(pat2).findall(page)
'''

code_US=[]
name_US=[]

for i in range(1,500):
    try:
        print("第"+str(i)+"页")
        url="http://97.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124002685751742868736_1563960115304&pn="+str(i)+"&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:105,m:106,m:107&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152"
        page = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
        print(len(page))
        pat1 = '"f12":"(.*?)"'  # 代码
        pat2 = '"f14":"(.*?)"'  # 名称

        res1 = re.compile(pat1).findall(page)
        res2 = re.compile(pat2).findall(page)

        code_US.extend(res1)
        name_US.extend(res2)

        time.sleep(2)


    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)


#港股和英股代码，开启多线程同时抓取
code_E = []
name_E = []

class E(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(1, 508):
            try:
                print("第" + str(i) + "页")
                url = "http://push2.eastmoney.com/api/qt/clist/get?cb=jQuery112403773894289652664_1563963743118&pn=" + str(i) + "&pz=20&po=1&fid=f3&np=1&ut=fa5fd1943c7b386f172d6893dbfba10b&fs=m:155+t:1,m:155+t:2,m:155+t:3,m:156+t:1,m:156+t:2,m:156+t:5,m:156+t:6,m:156+t:7,m:156+t:8&fields=f1,f14,f2,f4,f3,f17,f15,f16,f18,f20,f115,f13,f12,f152"
                page = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
                print(len(page))
                pat1 = '"f12":"(.*?)"'  # 代码
                pat2 = '"f14":"(.*?)"'  # 名称

                res1 = re.compile(pat1).findall(page)
                res2 = re.compile(pat2).findall(page)

                code_E.extend(res1)
                name_E.extend(res2)

                time.sleep(1)

            except urllib.error.URLError as e:
                if hasattr(e, "code"):
                    print(e.code)
                if hasattr(e, "reason"):
                    print(e.reason)


code_HK = []
name_HK = []

class HK(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(1, 104):
            try:
                print("第" + str(i) + "页")
                url = "http://41.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112407046227411048582_1564024920725&pn=" + str(i) + "&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:116+t:3&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152"
                page = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
                print(len(page))
                pat1 = '"f12":"(.*?)"'  # 代码
                pat2 = '"f14":"(.*?)"'  # 名称

                res1 = re.compile(pat1).findall(page)
                res2 = re.compile(pat2).findall(page)

                code_HK.extend(res1)
                name_HK.extend(res2)

                time.sleep(1)

            except urllib.error.URLError as e:
                if hasattr(e, "code"):
                    print(e.code)
                if hasattr(e, "reason"):
                    print(e.reason)


#开启线程
stock_E=E()
stock_E.start()

stock_HK=HK()
stock_HK.start()



#美股代码和名称写入文件
f=open("C:/Users/HL-lisa/Desktop/US.txt","w")
for i in range(len(code_us)):
    f.write(code_us[i])
    f.write('||')
    f.write(name_us[i])
    f.write('\n')
f.close()

#英股代码和名称写入文件
f=open("C:/Users/HL-lisa/Desktop/England.txt","w")
for i in range(len(code_E)):
    f.write(code_E[i])
    f.write('||')
    f.write(name_E[i])
    f.write('\n')
f.close()

#港股代码和名称写入文件
f=open("C:/Users/HL-lisa/Desktop/HK.txt","w")
for i in range(len(code_HK)):
    f.write(code_HK[i])
    f.write('||')
    f.write(name_HK[i])
    f.write('\n')
f.close()
