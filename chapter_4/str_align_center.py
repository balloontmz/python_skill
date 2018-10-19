#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'

s = "abc"

d = {
    "lodDist": 100.0,
    "SmallCull": 0.04,
    "DistCull": 500.0,
    "trilinear": 40,
    "farclip": 477
}

if __name__ == "__main__":
    # 第一种方式
    print(s.ljust(20), "*")  # 左对齐
    print(s.rjust(20), "*")  # 右对其，第二个参数为空格的最后一位填充的字符，类似分隔符
    print(s.center(20), "*")
    # 第二种方式 format方法
    print(format(s, "<20"))  # 左对齐
    print(format(s, ">20"))  # 右对齐
    print(format(s, "^20"))  # 居中对齐

    w = max(map(lambda x: len(x), d.keys()))
    for k in d:
        print(k.ljust(w), ":", d[k])
        # print(format(k, "<" + str(w)), ":", d[k])
