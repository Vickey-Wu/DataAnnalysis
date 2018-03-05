#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2017/12/9 17:15 
# @name: rental
# @author：vickey-wu


from lxml import etree
import requests
from requests.exceptions import ConnectionError
import pandas as pd
#获取目标网页的url
def get_page_index():
    base="https://sz.lianjia.com/zufang/baoanqu/rp"
    for i in range(1,10,1):
        url=base+str(i)+"/"
        yield url#yield为列表生成器


def get_page_detail(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            return etree.HTML(response.content.decode("utf-8"))
            #lxml.etree.HTML处理网页源代码会默认修改编码
        return None
    except ConnectionError:
        print ("Error occured")
        return None


#title为房屋标题；name为小区名称；catogery为房屋类别(几室几厅)
#size为房屋大小；region为区域；PV为看房人数；
#second_feature为高低楼层；third_feature为房屋建筑时间
def parse_page_detail(dom_tree):
    try:
        title=dom_tree.xpath('//li/div[2]/h2/a/text()')
        name=dom_tree.xpath('//li/div[2]//div/a/span/text()')
        catogery=dom_tree.xpath('//li/div[2]//div//span[1]//span/text()')
        size=dom_tree.xpath('//li/div[2]//div//span[2]/text()')
        region=dom_tree.xpath('//li/div[2]//div[1]//div[2]//div/a/text()')
        PV=dom_tree.xpath("//li/div[2]//div[3]//span[@class='num']/text()")
        price=dom_tree.xpath("//li/div[2]//div[2]//span[@class='num']/text()")
        date=dom_tree.xpath("//li/div[2]//div[2]//div[@class='price-pre']/text()")
        first_feature=dom_tree.xpath('//li/div[2]//div[1]//div[3]//span[@class="fang-subway-ex"]/span/text()')
        other=dom_tree.xpath('//li/div[2]//div[1]//div[2]//div/text()')
        name1=[]
        catogery1=[]
        size1=[]
        second_feature=[]
        third_feature=[]
        for n in name:
            name2=n[0:-2]
            name1.append(name2)
        for c in catogery:
            catogery2=c[0:-2]
            catogery1.append(catogery2)
        for s in range(0,59,2):
            size2=size[s][0:-2]
            size1.append(size2)
            second_feature1=other[s]
            second_feature.append(second_feature1)
        for m in range(1,60,2):
            third_feature1=other[m]
            third_feature.append(third_feature1)
        return {
            "title":title,
            "name":name1,
            "catogery":catogery1,
            "size":size1,
            "region":region,
            "price":price,
            "PV":PV,
            "second_feature":second_feature,
            "third_feature":third_feature,
           # "other":other
        }
    except:
        pass


df1=pd.DataFrame(columns=["title","name","catogery", "size","region","price","PV",
        "second_feature","third_feature"])      # ,"other"
i=0
if __name__=="__main__":
    urls=get_page_index()
    for url in urls:
        dom_tree=get_page_detail(url)
        result=parse_page_detail(dom_tree)
        print(result)
        df2=pd.DataFrame(result)
        df1=df1.append(df2,ignore_index=False,verify_integrity=False)
        i=i+1
        print(i) #打印出目前爬取的页数
    #保存数据到本地
    df1.to_csv("E:\\pythonProcess\\DataAnalysis\\result.csv")
    df1.info()
