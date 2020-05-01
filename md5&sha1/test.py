# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 13:08:54 2020

@author: yeshw
"""


import timeit

print (timeit.repeat(
"""
import hashlib
for line in url_paths:
#    h = hashlib.md5(line).hexdigest()
    h = hashlib.sha1(line).hexdigest()
"""
,
"""
url_paths = [l.encode('utf8') for l in open('galax.txt', 'r').readlines()]
""",))