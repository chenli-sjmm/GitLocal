#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: chenli
# project: SJMM

import urllib
import hashlib
import datetime
import json
from urllib.parse import unquote,quote
from test_data.get_data import *
from test_data.get_app_secret import *


class GetSign:
    def __init__(self):
        self.data = GetData()
        self.app_secret = GetSecret()
        self.header = GetHeards()


    def post_sign(self,row):
        headers = self.header.get_heard(row)
        headerData = headers['X-App-Id'] + "." + headers['X-Timestamp'] + "." + headers['X-Uniquely-Code'] + "." + \
                     headers[
                         'X-Nonce'] + "." + headers['X-Client-Type'] + "." + headers['X-App-Type'] + "." + headers[
                         'X-Auth-Token']
        URI = self.data.get_urls(row)
        appSecret = self.app_secret.get_secret(row)
        queryData = ''
        bodyData = json.dumps(self.data.get_body(row))
        signData = appSecret + "." + URI + "." + headerData + "." + queryData + "." + bodyData
        m = hashlib.md5()
        signDataEncode = urllib.parse.quote_plus(signData, safe='*').encode("utf-8")
        m.update(signDataEncode)
        sign = m.hexdigest()
        return sign

    def get_sign(self,row):
        """
            environment:环境
            URI：接口名（除去域名前的字段）
            payload：请求参数
            headers：请求头
            """
        headers = self.header.get_heard(row)
        headerData = headers['X-App-Id'] + "." + headers['X-Timestamp'] + "." + headers['X-Uniquely-Code'] + "." + \
                     headers[
                         'X-Nonce'] + "." + headers['X-Client-Type'] + "." + headers['X-App-Type'] + "." + headers[
                         'X-Auth-Token']
        URI = self.data.get_urls(row)
        appSecret = self.app_secret.get_secret(row)
        Data = json.dumps(self.data.get_body(row))
        query = []
        queryData = ''
        queryData_Uri = ''
        if Data != '':
            for i in Data.keys():
                query.append(i)
        query.sort()
        for i in query:
            queryData += i + '=' + str(Data[i])
            queryData_Uri += i + '=' + str(Data[i]) + '&'
        bodyData = ''
        signData = appSecret + "." + URI + "." + headerData + "." + queryData + "." + bodyData
        m = hashlib.md5()
        signDataEncode = urllib.parse.quote_plus(signData, safe='*').encode("utf-8")
        print(signDataEncode)
        m.update(signDataEncode)
        sign = m.hexdigest()
        return sign




if __name__ == '__main__':
    a = GetSign()
    print(a.get_sign(2))


