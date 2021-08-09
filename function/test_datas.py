#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: zengshaolin
# project: SJMM


import time

#  环境数据配置
configuration = 'UAT05'  # "DEV"|"SIT"|"UAT"

USER_NAME = 13919006845
PASSWORD = 123456
APP_VERSION = 3.1
now_time = time.time()

PAYLOAD = {"userName": USER_NAME, "password": PASSWORD, "cid": "edd0d4fc5b0f195a8a6ab3ed55e2ec1a"}    # cca5273762e8e5850bfedc5638bd0dd9   edd0d4fc5b0f195a8a6ab3ed55e2ec1a

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

SIT05_HEADERS = {
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

UAT05_HEADERS = {
    'X-App-Id': "116d70fb20eb6d1d7f053a74e2d807c1",
    'X-Timestamp': "%s" % now_time,
    'X-Uniquely-Code': "www",
    'X-Nonce': "%s" % now_time,
    'X-Client-Type': "ANDROID",
    'X-App-Type': "app_all_user",
    'X-Auth-Token': '',
    'Content-Type': "application/json; charset=utf-8",
    'X-App-Version': "%s" % APP_VERSION,
    'X-Cid': "fac1040c08e022969de9b8c6c93c7e94"}

UAT_HEADERS = {
    'X-Auth-Token': "",
    'Content-Type': "application/x-www-form-urlencoded",
    'X-Uniquely-Code': "www",
    'X-App-Type': "APP_ALL_USER",
    'X-App-Id': "116d70fb20eb6d1d7f053a74e2d807c1",
    'X-Timestamp': "%s" % now_time,
    'X-Nonce': "%s" % now_time,
    'X-Client-Type': "ANDROID",
    'X-App-Version': "%s" % APP_VERSION}


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

if configuration == "DEV":
    ENVIRONMENT = "DEV"
    HEADERS = DEV_HEADERS
    OLD_HEADERS = DEV_OLD_HEADERS
elif configuration == "UAT":
    ENVIRONMENT = "UAT"
    HEADERS = UAT_HEADERS
    OLD_HEADERS = UAT_OLD_HEADERS
elif configuration == "UAT05":
    ENVIRONMENT = "UAT05"
    HEADERS = UAT05_HEADERS
    OLD_HEADERS = SIT_OLD_HEADERS
elif configuration == "SIT":
    ENVIRONMENT = "SIT"
    HEADERS = SIT_HEADERS
    OLD_HEADERS = SIT_OLD_HEADERS
else:
    print("ERROR")


print(type(PAYLOAD))