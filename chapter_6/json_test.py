#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'

import json
import requests

d = {"b": None, "a": 5, "name": "bob"}

print(json.dumps(d, separators=[",", ":"], sort_keys=True))  # 将json中的分隔符后的空格去掉，能压缩json传输的数据大小

l1 = json.dumps(d, separators=[",", ":"], sort_keys=True)

l2 = json.loads(l1)

print(l2)

# load  dump  文件读写
with open("json_dump", "w") as f:
    json.dump(d, f)


if __name__ == "__main__":
    pass

