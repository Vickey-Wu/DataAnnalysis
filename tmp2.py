#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2017/11/4 23:08
# @name: tmp2
# @author：vickey-wu

import os
import re


def print_all_file_path(init_file_path, keyword):
    for current_dir, included_dir, included_file in os.walk(init_file_path):
        if included_file:
            for file in included_file:
                if re.search(keyword, file):
                    print(current_dir + "\\" + file)


def main():
    print_all_file_path("E:\pythonProcess\DataAnalysis", ".py")


if __name__ == '__main__':
    main()