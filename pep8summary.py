# !/usr/bin/python
# -*- coding:utf-8 -*-

# @filename: pep_summary
# @author：vickey wu
# @date: 2017/9/5 8:45

# Start at 5th Sep 2017
# Change at 6th Sep 2017 add Class and function summary


import os
import sys
from time import *
from subprocess import Popen, PIPE
from selenium.webdriver.support.wait import WebDriverWait

# long content cut to two or more part with "\"
content = "this is a very long long long long long\
 long long long long content long content"
slice_content = content[2:10:2]
print(slice_content)
length_con = len(content)
a, b, c = "", None, None

if 72 < length_con <= 120:
    if content == "this" and length_con == 80:
        length_cp = (length_con
                      + length_con
                      + length_con
                      + length_con)
        print(length_cp)

# different between "is" and "=="
if b is not c:
    print("different object")
else:
    print("same object")
if a == c:
    print("same value")
else:
    print("different value")

# different between "and" and "&"
aa, bb, cc = 1, 2, 1
if aa == 1 and bb == 2:
    print("'and' is logic operation, 1 treat as decimal 1")
if aa == 1 & cc == 1:
    print("'&' is bitwise operation, 1 treat as binary 01")
else:
    print("different")

try:
    aa == bb
except Exception as e:
    print("aa is not equal to bb")

# add whitespace at the lowest priorities
i = aa + bb
ii = (aa + bb) + aa * (bb + cc) + aa - bb


# Don't use spaces around the "=" when used to indicate a keyword argument or a default parameter value
def func(default_para1=1, para2=None):
    return func(1, None)


def func(default_para1=1, para2=None):
    return func(1, None)


class Class_(TypeError):
    """
    This Class used to practice pep8 regulation
    """

    def __init__(self, para1, ):
        self.para1 = para1

    def class_func1(self, para_f1, ):
        para_f1 = self.para1
        return para_f1

    def _class_func1(self, para_f1, ):
        _para_f1 = self.para1


# name suffix or prefix with double "__" single "_"
# one underline in the beginning indicate this method or attribute is private
# which mean other method can\'t call it

# one underline in the end avoid name is conflict with keyword
# two underline in the beginning and in the end to avoid Class be overridden by subClass
