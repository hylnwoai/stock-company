#第一次使用github

目标：抓取港股&美股&英股的上市公司详情页

首先，从东方财富网抓取列表页，代码为code.py
股票代码的列表分别保存在HK，US，England（突然忘记了英国的简称）三个文本文件中,在压缩包中

之所以这么麻烦，是因为同花顺网站的列表页反爬有点变态，我破解不了，cookie只能抓取5页就失效了
只好采用曲线救国的办法了，在别的财经网页抓取列表页，再在同花顺抓取详情页


其次，在同花顺抓取详情页

注：港股 和 美英股的公司详情页布局不一致

港股公司详情页抓取代码为company_hk.py

美股公司详情页抓取代码为company_us&uk.py


