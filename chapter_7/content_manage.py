#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
我们实现了一个telnet客户端的类TelnetClient，调用实例的start（）方法启动客户端与服务器交互，
交互完毕后需调用clearup（）方法，关闭已连接的socket，以及将操作历史记录写入文件并关闭。

能否让TelnetClient的实例支持上下文管理协议，从而替代手工调用clearup（）方法
"""

__author__ = 'tomtiddler'

from telnetlib import Telnet
from sys import stdin, stdout
from collections import deque
from contextlib import contextmanager


class TelnetClient(object):
    def __init__(self, addr, port=23):
        self.addr = addr
        self.port = port
        self.tn = None

    def start(self):
        self.tn = Telnet(self.addr, self.port)
        self.history = deque()

        # user
        t = self.tn.read_until(b"login: ")
        stdout.write(t.decode())
        user = stdin.readline().encode()
        self.tn.write(user)

        # password
        t = self.tn.read_until(b"Password: ")
        if t.startswith(user[:-1]):
            t = t[len(user) + 1:]
        stdout.write(t.decode())
        self.tn.write(stdin.readline().encode())

        t = self.tn.read_until(b"$ ")
        stdout.write(t.decode())
        while True:
            uinput = stdin.readline()
            if not uinput:
                break
            self.history.append(uinput)
            self.tn.write(uinput.encode())
            t = self.tn.read_until(b"$ ").decode()
            stdout.write(t[len(uinput) + 1:])

    def cleanup(self):
        self.tn.close()
        self.tn = None
        with open(self.addr + "_history.txt", "w") as f:
            f.writelines(self.history)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # 异常类型，异常值，异常栈
        self.tn.close()
        self.tn = None
        with open(self.addr + "_history.txt", "w") as f:
            f.writelines(self.history)
        if exc_type:  # 模拟处理异常
            print(exc_tb)
            return True


if __name__ == "__main__":
    # client = TelnetClient("127.0.0.1")
    # print("start...")
    # client.start()
    # print("clearup...")
    # client.cleanup()

    # 标准的上下文管理器，实现了__enter__ 和 __exit__ 方法
    with TelnetClient("127.0.0.1") as client:
        client.start()

    # 装饰器的形式实现的上下文管理，yield第一次返回对象，第二次进入调用yield之后的内容
    # 采用的 yield 关键字 联想到了消费者-生产者模型， yield 和send

    @contextmanager
    def created_client():
        client = TelnetClient("127.0.0.1")
        yield client
        client.cleanup()

    with created_client() as client2:
        client2.start()

    # 同时，对于定义了 close() 方法的类，能通过contextlib.closing() 实现上下文管理，
    # 此处只需要将cleanup() 函数重命名即可
    from contextlib import closing

    with closing(TelnetClient("127.0.0.1")) as client:
        client.start()
