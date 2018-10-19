#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'

import re
from collections import Iterable

# s = """
# Django has a lot of documentation. A high-level overview of how it’s organized will help you
# know where to look for certain things:
# """
# print(s.split())


def my_split(s, ds):
    res = [s]
    for d in ds:
        t = []
        list(map(lambda x: t.extend(x.split(d)), res))  # map函数是惰性的，需要显式迭代取值才能运行。
        res = t
    return [x for x in res if x]  # 去除空字符串，不是空格


if __name__ == "__main__":
    s = "www@muke-62-4595;871-bpjij:;/data/webroot,,, ,$ www@muke-62-4595871-bpjij:/data/webroot$"
    print(my_split(s, ";,|\t"))
    resu = re.split("[,;\t|]+", s)
    print(resu)

