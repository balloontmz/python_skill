#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
实现历史记录
"""

__author__ = 'tomtiddler'

from random import randint
from collections import deque  # 队列
import pickle, json

N = randint(0, 100)
history = deque([], 5)


def guess(k):
    if k == N:
        print("right")
        return True
    if k < N:
        print("%s is less than N" % k)
    else:
        print("%s is better than N" % k)
    return False


if __name__ == "__main__":
    while True:
        line = input("please input a number:")
        if line.isdigit():
            k = int(line)
            history.append(k)
            if guess(k):
                break
        if line == "help":
            print(list(history))
        if line == "save":
            with open("history2.txt", "w") as fi:
                # pickle.dump(history, fi)
                json.dump(list(history), fi)
        if line == "open":
            with open("history2.txt", "r") as fi:
                history = deque(json.load(fi), 5)
