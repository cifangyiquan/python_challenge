#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 cifangyiquan.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: 7.py
Author: work(work@cifangyiquan)
Date: 2017/08/14 19:45:48
"""


import cv2 
import numpy as np
import re

img = cv2.imread('oxygen.png')

(rows, columns, channels) = img.shape

px = img[rows/2, :]

row = px[::7]

ords = [r for r, g, b in row if r == g ==b]

out = "".join(map(chr, ords))

nums = re.findall("\d+", "".join(map(chr, ords)))

ret = "".join(map(chr, map(int, nums)))
print ret 



#for pixel in px:
#    print pixel
