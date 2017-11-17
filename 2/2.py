#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 cifangyiquan.com, Inc. All Rights Reserved
# 
########################################################################

"""
File: 3.py
Author: work(work@cifangyiquan)
Date: 2017/08/11 01:11:21
"""
stat = {}

fp = open('2.input')
ret = ''
for line in fp:
    line = line.strip()
    for ch in line:
        if ch in stat:
            stat[ch] += 1
        else:
            stat[ch] = 1
        if ord('a') <= ord(ch) <= ord('z'):
            ret += ch

for key, value in stat.items():
    print key + '\t' + str(value)

print ret
