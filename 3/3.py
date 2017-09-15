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
Date: 2017/08/12 00:48:45
"""
import re

fp = open('4.input')
ret = ""
for line in fp:
    line = line.strip()
    m = re.match(r'.*[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', line)
    if m:
        ret += m.group(1)

print ret
