#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'

from urllib.request import urlretrieve
import csv

# urlretrieve("http://table.finance.yahoo.com/table.csv?s=000001.sz", "pingan.csv")  # 不可用

rf = open("pufa.csv", "rb")
reader = csv.reader(rf)  # 迭代器对象

for row in reader: pass

wf = open("pufa_copy.csv", "wb")
writer = csv.writer(wf)
writer.writerow([])  # 接收一行
wf.flush()  # 刷新缓存区？

# 如何读写csv文件，对csv文件中成交值大于5千万的交易存储到另一个csv文件中。并且年份为大于2016年
with open("pufa.csv", "wb") as rf:
    reader = csv.reader(rf)
    with open("pufa_copy.csv", "wb") as wf:
        writer = csv.writer(wf)
        headers = reader.next()
        writer.writerow(headers)
        for row in reader:
            if row[0] < '2016-01-01':
                break
            if int(row[5]) >= 50000000:
                writer.writerow(row)
print("end")

if __name__ == "__main__":
    pass

