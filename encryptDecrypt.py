#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2017/11/7 21:42 
# @name: encryptDecrypt
# @author：vickey-wu


import crypt
import random,string

def getsalt(chars = string.letters+string.digits):
    return random.choice(chars)+random.choice(chars)

salt = getsalt()
print salt
print crypt.crypt('bananas',salt)

