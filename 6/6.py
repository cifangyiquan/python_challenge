#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 cifangyiquan.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: 6.py
Author: work(work@cifangyiquan)
Date: 2017/08/14 16:42:48
"""
import zipfile

zf = zipfile.ZipFile('./channel.zip', 'r')

name = '90052.txt'
comments = ''
while True:
    data = zf.read(name)
    comments += zf.getinfo(name).comment
#print data
    text = data.strip().split(' ')
    print text
    if len(text) <= 3:
        break
    name = text[3] + '.txt'

print comments
