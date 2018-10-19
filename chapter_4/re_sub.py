#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'

import re

s = """
2016-08-03
2017-09-02
"""

# 正则表达式的字符串替换方法 sub  以及捕获组 group
# resu = re.sub("(\d{4})-(\d{2})-(\d{2})", r"\2/\3/\1", s)
resu = re.sub("(?P<year>\d{4})-(?P<m>\d{2})-(?P<d>\d{2})", r"\g<m>/\g<d>/\g<year>", s)

if __name__ == "__main__":
    print(resu)

