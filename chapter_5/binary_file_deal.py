#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
如何用python处理二进制媒体文件
通过格式能够通用于很多媒体文件
本此主要通过对二进制文件的读写完成了data数据的减小，从而减小音频文件的声音大小
主要用到struct包

"""

__author__ = 'tomtiddler'

import struct
import array

if __name__ == "__main__":
    with open("wav4test.wav", "rb") as f:
        info = f.read(46)
        print(info)
        print(struct.unpack("<h", info[22:24]))  # 小端，默认的也是小端
        print(struct.unpack("<i", info[24:28]))  # 采样频率
        print(struct.unpack("<h", info[34:36]))  # 编码宽度
        f.seek(0, 2)  # 文件指针的相关操作，没有理解透彻。
        f.tell()  # 文件目前指针位置。
        n = int((f.tell()-45)/2)  # 文件的数据长度，每个数据元两个长度
        # print(n)
        buf = array.array("h")  # 采用数组，相对于列表，能够节省辅助空间。但是数组的功能较为有限
        index = 0
        f.seek(46)

        for x in range(n):
            buf.append(struct.unpack("<h", f.read(2))[0])  # 为数组追加数据值，初始化数组并替换的操作未完成，需要查看文档相关功能
        # print(buf[0])
        # print(buf[5])

        for i in range(n):
            # 通过压缩数据的值减小声音，效果不佳，这个需要多了解才能知道原因
            # 上面那条作废，主要原因还是位数取错了，导致了错位，从而导致声音效果不佳，通过改正修改位置，减音量效果比较明显。
            buf[i] //= 2
        print(len(buf))

    with open("demo.wav", "wb") as f2:
        # f2.write(info)
        # buf.tofile(f2)

        # 自己实现的类似tofile的功能
        li = []
        for buf_ in buf:
            li.append(struct.pack("<h", buf_))
        initi = b"".join(li)  # join能显著提升字节拼接速度
        # print(struct.pack("<h", buf[3000]))
        f2.write(info + initi)

