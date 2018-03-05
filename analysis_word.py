#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2017/9/10 22:36
# @name: tmpTest
# @author：vickey-wu


# numpy
import numpy as np

arr_d1 = np.array([2, 0, 1.11, 7])
print(arr_d1)

arr_d2 = np.array([[1, 2, 4, 3.1], [3, 4, 5, 8]])
print(arr_d2*arr_d2)

# set as 2d at lest
# arr_d2_min = np.array([2, 3], ndmin=2)
arr_d2_min = np.array([[2, 3], [4, 5]])
print(arr_d2_min)
# matrix
matrix = np.array(np.mat('2, 3;4 5'))
print(matrix)
print(np.array(np.mat("1;3"), subok=True))

# complex num
arr_complex = np.array([1, 2, 3], dtype=complex)
print(arr_complex)


