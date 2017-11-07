#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2017/9/27 23:06 
# @name: pandas_test
# @author：vickey-wu

import pandas as pd




data_list = ["a", "b", "?", "c"]
data_dict = {'a': 0.00, 'b': 1, 'c': 2.222}
data_constant = 666
index = ["b", "c", "d", "e", "f"]

s1 = pd.Series(data_dict, index)
s2 = pd.Series(data_constant, index)
# print(s1, "data_dict")
# print(s2, "data_constant")
# print(s1[-2:], "last two data")
# print(s1[["c", "d"]], "index c and d's data")

# if data is a dict or constant no need to do follow operation
if len(data_list) < len(index):
    distance = len(index) - len(data_list)
    for i in range(distance):
        data_list.append("no_value")
    s = pd.Series(data_list, index)
    # print(s)
if len(data_list) > len(index):
    distance = len(data_list) - len(index)
    for i in range(distance):
        index.append("no_index")
    s = pd.Series(data_list, index)
    # print(s)
else:
    s = pd.Series(data_list, index)
    # print(s)


data_df_list = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
data_df_dict = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28, 34, 29, 42]}
df_list = pd.DataFrame(data_df_list, index=['Name', 'Age', 'Sex'], dtype=float)
df_dict = pd.DataFrame(data_df_dict, columns=['Name', 'Age', 'Sex'], dtype=float)
print(df_list, "data_list")
print(df_dict, "data_dict")
