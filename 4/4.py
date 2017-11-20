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
import re
import traceback
import sys
import time

try:
    nothing = '12345'
    for i in range(400):
        url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nothing
        print url
        time.sleep(0.5)
        r = requests.get(url)
        line = r.text
        print line
        m = re.match(r'.*?(\d+)', line)
        if m:
            nothing = m.group(1)
        else:
            print line
            break
except:
    traceback.print_exc(limit=2, file=sys.stderr)
