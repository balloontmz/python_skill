#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
可迭代对象和迭代器对象
"""

__author__ = 'tomtiddler'

from collections import Iterable, Iterator

import requests

# l = [1, 2, 3, 4]
#
# s = "abcdefg"
#
# for x in l:
#     print(x)
#
# print(isinstance(l, Iterable))


class WeatherIterator(Iterator):
    """实现一个迭代器对象，next方法每次返回一个城市气温"""

    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def get_weather(self, city):
        """获取天气信息"""
        r = requests.get("http://wthrcdn.etouch.cn/weather_mini?city=" + city)
        data = r.json()["data"]["forecast"][0]
        return "%s %s %s " % (city, data["low"], data["high"])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)

    def __iter__(self):
        return self


class WeatherIterable(Iterable):
    """实现一个可迭代对象，__iter__方法返回一个迭代器对象"""
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


if __name__ == "__main__":
    # print(get_weather("北京"))
    # print(get_weather("长沙"))
    l = ["北京", "长沙", "上海", "杭州"]
    weather = WeatherIterable(l)
    for x in weather:
        print(x)
    weather2 = WeatherIterator(l)
    for y in weather2:
        print(y)

