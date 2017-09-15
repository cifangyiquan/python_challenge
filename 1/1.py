#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 cifangyiquan.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: 2.py
Author: work(work@cifangyiquan)
Date: 2017/08/11 00:45:45
"""
import string

input = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
input = 'map'
ret = ''
for i in input:
    num = ord(i)
    if ord('a') <= num <= ord('x'):
        char = chr(num + 2)
    elif ord('y') <= num <= ord('z'):
        char = chr(num - 26 + 2)
    else:
        char = i
    ret += char


print ret

