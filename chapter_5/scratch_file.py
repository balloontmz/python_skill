#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'

from tempfile import TemporaryFile, NamedTemporaryFile

"""关闭之后自动删除"""
f = TemporaryFile()

f.write(b"abcdef" * 100000)

f.seek(0)

print(f.read(100))

f = NamedTemporaryFile(delete=False)  # delete指定关闭之后是否删除
# 命名的临时文件有一个好处就是能够多进程通过路径访问，而且能指定是否删除
print(f.name)

if __name__ == "__main__":
    pass

