#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: chenli
# project: SJMM

import time
from function.operation_excel import OperationExcel
from test_data.data_config import *


class GetHeards:
    #  环境数据配置
    APP_VERSION = 3.1
    now_time = time.time()
    DEV_HEADERS = {
        'X-Auth-Token': "",
        'Content-Type': "application/json; charset=utf-8",
        'X-Uniquely-Code': "www",
        'X-App-Type': "APP_ALL_USER",
        'X-App-Id': "b1bec9cfab5d5c3af910534034fe3b16",
        'X-Timestamp': "%s" % now_time,
        'X-Nonce': "%s" % now_time,
        'X-Client-Type': "ANDROID",
        'X-App-Version': "%s" % APP_VERSION}
    SIT_HEADERS = {
        'X-Auth-Token': '',
        'Content-Type': "application/json; charset=utf-8",
        'X-Uniquely-Code': "www",
        'X-App-Type': "APP_ALL_USER",
        'X-App-Id': "8d287102e8e637af8cf7a4cdc13dd1a8",
        'X-Timestamp': "%s" % now_time,
        'X-Nonce': "%s" % now_time,
        'X-Client-Type': "ANDROID",
        'X-App-Version': "%s" % APP_VERSION}
    UAT_HEADERS = {
        'X-Auth-Token': "",
        'Content-Type': "application/json; charset=utf-8",
        'X-Uniquely-Code': "www",
        'X-App-Type': "APP_ALL_USER",
        'X-App-Id': "116d70fb20eb6d1d7f053a74e2d807c1",
        'X-Timestamp': "%s" % now_time,
        'X-Nonce': "%s" % now_time,
        'X-Client-Type': "ANDROID",
        'X-App-Version': "%s" % APP_VERSION}
    DEV_NEW_HEADERS = {
        'X-App-Id': "b1bec9cfab5d5c3af910534034fe3b16",
        'X-Timestamp': "%s" % now_time,
        'X-Uniquely-Code': "www",
        'X-Nonce': "%s" % now_time,
        'X-Client-Type': "ANDROID",
        'X-App-Type': "app_all_user",
        'X-Auth-Token': '',
        'Content-Type': "application/json; charset=utf-8",
        'X-App-Version': "%s" % APP_VERSION,
        'X-Cid': "b1bec9cfab5d5c3af910534034fe3b16"}
    SIT_NEW_HEADERS = {
        'X-App-Id': "8d287102e8e637af8cf7a4cdc13dd1a8",
        'X-Timestamp': "%s" % now_time,
        'X-Uniquely-Code': "www",
        'X-Nonce': "%s" % now_time,
        'X-Client-Type': "ANDROID",
        'X-App-Type': "app_all_user",
        'X-Auth-Token': '',
        'Content-Type': "application/json; charset=utf-8",
        'X-App-Version': "%s" % APP_VERSION,
        'X-Cid': "8d287102e8e637af8cf7a4cdc13dd1a8"}
    UAT_NEW_HEADERS = {
        'X-App-Id': "116d70fb20eb6d1d7f053a74e2d807c1",
        'X-Timestamp': "%s" % now_time,
        'X-Uniquely-Code': "www",
        'X-Nonce': "%s" % now_time,
        'X-Client-Type': "ANDROID",
        'X-App-Type': "app_all_user",
        'X-Auth-Token': '',
        'Content-Type': "application/json; charset=utf-8",
        'X-App-Version': "%s" % APP_VERSION,
        'X-Cid': "116d70fb20eb6d1d7f053a74e2d807c1"}
    DEV_OLD_HEADERS = {
        'X-Auth-Token': "",
        'Content-Type': "application/x-www-form-urlencoded; charset=utf-8",
        'X-Uniquely-Code': "www",
        'X-App-Type': "APP_ALL_USER",
        'X-App-Id': "b1bec9cfab5d5c3af910534034fe3b16",
        'X-Timestamp': "%s" % now_time,
        'X-Nonce': "%s" % now_time,
        'X-Client-Type': "ANDROID",
        'X-App-Version': "%s" % APP_VERSION}
    SIT_OLD_HEADERS = {
        'X-Auth-Token': "",
        'Content-Type': "application/x-www-form-urlencoded; charset=utf-8",
        'X-Uniquely-Code': "www",
        'X-App-Type': "APP_ALL_USER",
        'X-App-Id': "",
        'X-Timestamp': "%s" % now_time,
        'X-Nonce': "%s" % now_time,
        'X-Client-Type': "ANDROID",
        'X-App-Version': "%s" % APP_VERSION}
    UAT_OLD_HEADERS = {
        'X-Auth-Token': "",
        'Content-Type': "application/x-www-form-urlencoded; charset=utf-8",
        'X-Uniquely-Code': "www",
        'X-App-Type': "APP_ALL_USER",
        'X-App-Id': "",
        'X-Timestamp': "%s" % now_time,
        'X-Nonce': "%s" % now_time,
        'X-Client-Type': "ANDROID",
        'X-App-Version': "%s" % APP_VERSION}

    def __init__(self, heard=None):
        self.opera_excel = OperationExcel()
        self.data_config = GlobalVar()
        self.heard = heard

    def get_heard(self, row):
        col = int(self.data_config.get_heard())
        heard = self.opera_excel.get_cell_value(row, col)
        if heard == "DEV":
            dev_heard = GetHeards.DEV_HEADERS
            return dev_heard
        elif heard == "SIT":
            sit_heard = GetHeards.SIT_HEADERS
            return sit_heard
        elif heard == "UAT":
            uat_heard = GetHeards.UAT_HEADERS
            return uat_heard
        elif heard == "NEW_DEV":
            sit_heard = GetHeards.DEV_NEW_HEADERS
            return sit_heard
        elif heard == "NEW_SIT":
            sit_heard = GetHeards.SIT_NEW_HEADERS
            return sit_heard
        elif heard == "NEW_UAT":
            sit_heard = GetHeards.UAT_NEW_HEADERS
            return sit_heard
        elif heard == "OLD_DEV":
            sit_heard = GetHeards.DEV_OLD_HEADERS
            return sit_heard
        elif heard == "OLD_SIT":
            sit_heard = GetHeards.SIT_OLD_HEADERS
            return sit_heard
        elif heard == "OLD_UAT":
            sit_heard = GetHeards.UAT_OLD_HEADERS
            return sit_heard
        else:
            print("ERROR")



if __name__ == '__main__':
    a = GetHeards()
    print(a.get_heard(1))
