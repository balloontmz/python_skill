#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
复制的语音识别代码。
"""

__author__ = 'tomtiddler'

import requests
import json

from record import Record
record = Record(channels=1)
audiaData = record.record(2)

API_KEY = ""
SECRET_KEY = ""

# 获取token
authUrl = ""
res = requests.get(authUrl)
token = res["access_token"]

# 语音识别
cuid = ""
srvUrl = ""
httpHeader = {

}


if __name__ == "__main__":
    pass

