#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2017/9/14 9:03 
# @name: K-MeansPractice
# @author：vickey-wu

# practice of K-Means algorithm

import pandas as pd
from sklearn.cluster import KMeans


input_flie = "E:/pythonProcess/chapter5/demo/data/consumption_data.xls"
output_file = "E:/pythonProcess/chapter5/demo/data/consumption_result.xls"

# cluster category
k = 3
# iteration os cluster
iteration = 500

data = pd.read_excel(input_flie, index_col="Id")
# standardization data
data_zs = 1.0 * (data-data.mean())/data.std()

# separate as "k" clusters and "4" erupt simultaneously and iteration equal to "iteration"
model = KMeans(n_clusters=k, n_jobs=4, max_iter=iteration)
# begin to cluster
model.fit(data_zs)

# count nums of each category
category_num = pd.Series(model.labels_).value_counts()
# find cluster center
cluster_center = pd.DataFrame(model.cluster_centers_)
# horizontal connect data to get num of category of cluster center
r = pd.concat([category_num, cluster_center], axis=1)
r.columns = list(data.columns) + ["category_num"]

# print each sample's category
r = pd.concat([data, pd.Series(model.labels_, index=data.index)], axis=1)
r.columns = list(data.columns) + ["category_cluster"]
r.to_excel(output_file)

#
# #使用K-Means算法聚类消费行为特征数据
#
# import pandas as pd
#
#
# def k_means():
#     #参数初始化
#     inputfile = 'E:/pythonProcess/chapter5/demo/data/consumption_data.xls' #销量及其他属性数据
#     outputfile = 'E:/pythonProcess/chapter5/demo/data/data_type.xls' #保存结果的文件名
#     k = 3 #聚类的类别
#     iteration = 500 #聚类最大循环次数
#     data = pd.read_excel(inputfile, index_col='Id') #读取数据
#     data_zs = 1.0*(data - data.mean())/data.std() #数据标准化
#
#     from sklearn.cluster import KMeans
#     model = KMeans(n_clusters = k, n_jobs = 4, max_iter = iteration) #分为k类，并发数4
#     model.fit(data_zs) #开始聚类
#
#     #简单打印结果
#     r1 = pd.Series(model.labels_).value_counts() #统计各个类别的数目
#     r2 = pd.DataFrame(model.cluster_centers_) #找出聚类中心
#     r = pd.concat([r2, r1], axis = 1) #横向连接（0是纵向），得到聚类中心对应的类别下的数目
#     r.columns = list(data.columns) + [u'类别数目'] #重命名表头
#     print(r)
#
#     #详细输出原始数据及其类别
#     r = pd.concat([data, pd.Series(model.labels_, index = data.index)], axis = 1)  #详细输出每个样本对应的类别
#     r.columns = list(data.columns) + [u'聚类类别'] #重命名表头
#     r.to_excel(outputfile) #保存结果
#
#     density_plot(data, k)
#
#     pic_output = 'E:/pythonProcess/chapter5/demo/data/pd_'  # 概率密度图文件名前缀
#     for i in range(k):
#         density_plot(data[r[u'聚类类别'] == i], k).savefig(u'%s%s.png' % (pic_output, i))
#
#
# def density_plot(data, k): #自定义作图函数
#       import matplotlib.pyplot as plt
#       plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
#       plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
#       p = data.plot(kind='kde', linewidth = 2, subplots = True, sharex = False)
#       [p[i].set_ylabel(u'密度') for i in range(k)]
#       plt.legend()
#       return plt
#
#
# if __name__ == '__main__':
#     k_means()