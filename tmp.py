#!/usr/bin/env python
# -*- coding:utf-8 -*-
# socket server.py

p = "vickey"
shift_nums = 168
for ii in p:
    print(ord(ii))
# print(int(str(shift_nums)[1]))
def vickey_ecrypt(p, shift_nums):
    tmp_l = []
    for n in range(len(str(shift_nums))):
        for s in p:
            bit_oper = ord(s)
            if int(str(shift_nums)[n]) <= 5:
                bit_oper <<= int(str(shift_nums)[n])
            else:
                bit_oper >>= int(str(shift_nums)[n])
            encrypt_str = unichr(bit_oper)
            # print(type(encrypt_str), encrypt_str)
            tmp_l.append(encrypt_str)
        p = "".join(tmp_l)
        tmp_l = []
    return p

vickey_ecrypt(p, shift_nums)

def vickey_decrypt(p, shift_nums):
    pd = vickey_ecrypt(p, shift_nums)
    tmp_l = []
    for n in range(len(str(shift_nums))):
        for s in p:
            bit_oper = ord(s)
            if int(str(shift_nums)[n]) > 5:
                bit_oper <<= int(str(shift_nums)[n])
            else:
                bit_oper >>= int(str(shift_nums)[n])
            encrypt_str = unichr(bit_oper)
            # print(type(encrypt_str), encrypt_str)
            tmp_l.append(encrypt_str)
        p = "".join(tmp_l)
        tmp_l = []
    return p

