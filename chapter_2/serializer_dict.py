#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'

from collections import OrderedDict
from time import time, sleep
from random import randint

# d = OrderedDict()
# d["JIn"] = (1, 35)
# d["Leo"] = (2, 40)
# d["Tom"] = (3, 45)

d = OrderedDict()
players = list("ABCDEFGH")
start = time()

for i in range(8):
    sleep(randint(0, 10)/10)
    p = players.pop(randint(0, 7 - i))
    end = time()
    print(i + 1, p, end - start)
    d[p] = (i + 1, end - start)

print("-"*30)
for k in d:
    print(k, d[k])

# 一个先进先出的字典，有序字典。
# class LastUpdatedOrderedDict(OrderedDict):
#
#     def __init__(self, capacity):
#         super(LastUpdatedOrderedDict, self).__init__()
#         self._capacity = capacity
#
#     def __setitem__(self, key, value):
#         containsKey = 1 if key in self else 0
#         if len(self) - containsKey >= self._capacity:
#             last = self.popitem(last=False)
#             print('remove:', last)
#         if containsKey:
#             del self[key]
#             print('set:', (key, value))
#         else:
#             print('add:', (key, value))
#         OrderedDict.__setitem__(self, key, value)


if __name__ == "__main__":
    pass

