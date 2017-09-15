#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 cifangyiquan.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: 4.py
Author: work(work@cifangyiquan)
Date: 2017/08/12 01:23:28
"""

import requests

nothing = '12345'
for i in range(400):
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nothing
    print url
    r = requests.get(url)
    line = r.text
    ret_list = line.strip().split(' ')
    nothing = ret_list[5]
    print line
print line
