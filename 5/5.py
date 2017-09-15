#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 cifangyiquan.com, Inc. All Rights Reserved
# 
########################################################################

"""
File: 5.py
Author: work(work@cifangyiquan)
Date: 2017/08/12 01:42:09
"""

import requests
import pickle

r = requests.get('http://www.pythonchallenge.com/pc/def/banner.p')
ret = pickle.loads(r.text)

for ch in ret:
    # print("".join([k * v for k, v in ch]))
    ret = ''
    for k, v in ch:
        ret += k * v
    print  ret
