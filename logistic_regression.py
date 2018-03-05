#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2017/11/30 23:52 
# @name: logistic_regression
# @author：vickey-wu

import pandas as pd
import numpy as np

def sigmoid(x):
    """
    sigmoid function
    :return: 
    """
    return 1.0 / (1 + np.exp(-x))


def error_rate():
    pass


def lr_train_bgd(feature, label, maxCycle, alpha):
    """
    logistic regression train batch gradient descent
    :param feature: mat
    :param label: mat
    :param maxCycle: int
    :param alpha: float
    :return: weight: mat
    """
    n = np.shape(feature)
    w = np.mat(np.ones(n, 1))
    i = 0
    while i <= maxCycle:
        i += 1
        h = sigmoid(feature * w)
        err = label - h
        if i % 100 == 0:
            print(str(i) + str(error_rate(h, label)))
        w = w + alpha * feature * err
    return w


def load_data(file_name):
    """
    input: file_name(str)
    output: feature_data(mat)
            label_data(mat)
    :param file_name: 
    :return: 
    """
    f = open(file_name)