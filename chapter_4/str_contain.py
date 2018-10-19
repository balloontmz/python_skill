#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
判断字符串开头与结尾
"""

__author__ = 'tomtiddler'

import os, stat

# str.startswith()
# str.endswith()

d = os.listdir(".")

if __name__ == "__main__":
    # print(d)
    for name in d:
        if name.endswith((".sh", ".py")):
            # print(oct(os.stat(name).st_mode))  #
            os.chmod(name, os.stat(name).st_mode | stat.S_IXUSR)  # 更改文件的执行权限


