#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
如何在python中为文件设置缓冲行为？
"""

__author__ = 'tomtiddler'

import mmap

# python默认缓冲区大小为  本机为 8 * 1024 可为open对象设置buffering指定缓冲区大小，
# 缓冲区大小设置为1,则是行缓冲。只有遇到类似换行符才会提交缓冲
# 无缓冲 -- buffering设置为0 会实时地存储到磁盘当中

if __name__ == "__main__":
    f = open("demo.bin", "r+b")
    # f.fileno()  # 报告一个文件描述符  等同于os.open
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)  # 映射区域长度  0 代表全部  access 访问权限 write  写
    print(m[0])
    print(m[10:20])
    m[0] = int("88", 16)
    m[4:8] = b'\xff' * 4
    # offset 指定跳过映射文件的某个区域--需要是页面的整数倍，区域长度为8页
    m = mmap.mmap(f.fileno(), mmap.PAGESIZE*8, access=mmap.ACCESS_WRITE, offset=mmap.PAGESIZE*4)
    m[:0x1000] = b"\xaa" * 0x1000
    f.close()


