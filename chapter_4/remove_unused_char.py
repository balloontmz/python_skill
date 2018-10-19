#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'

import re

s = "   abc   "
s2 = "----abc++++"
s3 = "abc:123"
s4 = "\tabc\t123\txyz"
s5 = "\tabc\t123\txyz\r"
s6 = "abc123xyz"

if __name__ == "__main__":
    s.strip()  # 可指定字符，在两端删除，默认为空格
    s.lstrip()  # 左端
    s.rstrip()  # 右端
    s2.strip("-+")  # 去掉加减号，不再去除默认的空格

    s_ = s3[:3] + s3[4:]

    s4.replace("\t", "")  # 一次只能替换一种
    s_5 = re.sub("[\t\r]", "", s5)  # 一次能替换多种

    # 创建映射字典，值可映射为None，可用于字符串加密。加密解密两边采用同样的映射表就行了，只能单个字符进行映射。不能一对多或者多对一
    m = str.maketrans({"a": "x", "b": "y", "c": "z"})
    print(s6.translate(m))  # 采用映射字典进行映射
