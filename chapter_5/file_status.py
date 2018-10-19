#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'

import os
import stat
import time

if __name__ == "__main__":
    print(os.stat("demo.bin"))
    os.lstat("demo.bin")  # 不跟随符号链接--对于软链接，取到的是它本身的状态

    f = open("demo.bin", "r")
    os.fstat(f.fileno())  # 和stat类似，但是需要传入文件描述符
    f.close()

    s = os.stat("demo.bin")
    print(stat.S_ISDIR(s.st_mode))  # 判断文件类型  具体查看文档

    # 判断权限，大于零代表有权限。等于零代表没权限。二进制的与运算 具体参数查看文档  linux命令ll查看权限
    print(s.st_mode & stat.S_IXUSR)

    print(time.localtime(s.st_atime))  # 查看最后修改时间

    print(s.st_size)  # 查看文件大小

    # 通过os.path进行操作
    print(os.path.isdir("demo.bin"))
    print(os.path.isfile("demo.bin"))  # 文件类型  没有文件访问权限接口

    print(os.path.getatime("demo.bin"))  # 修改时间

    print(os.path.getsize("demo.bin"))  # 查看文件大小



