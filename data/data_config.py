#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:chen_li
# project: SJMM


class GlobalVar:
    id = '0'
    name = '1'
    domian = '2'
    gateway = '3'
    heard = '4'
    url = '5'
    is_run = '6'
    depend_id = '7'
    depend_data = '8'
    depend_value = '9'
    body = '10'
    expected_result = '11'
    result = '12'

    # 获取case_id
    def get_id(self):
        return GlobalVar.id

    # 获取接口名称
    def get_name(self):
        return GlobalVar.name

    # 获取测试环境
    def get_domian(self):
        return GlobalVar.domian

    # 获取请求方式
    def get_gateway(self):
        return GlobalVar.gateway

    # 获取heard
    def get_heard(self):
        return GlobalVar.heard

    # 获取url
    def get_url(self):
        return GlobalVar.url

    # 获取是否执行
    def get_is_run(self):
        return GlobalVar.is_run

    # 获取依赖id
    def get_depend_id(self):
        return GlobalVar.depend_id

    # 获取依赖数据
    def get_depend_data(self):
        return GlobalVar.depend_data

    # 获取依赖字段
    def get_depend_value(self):
        return GlobalVar.depend_value

    # 获取请求参数
    def get_body(self):
        return GlobalVar.body

    # 获取预期结果值
    def get_expected_result(self):
        return GlobalVar.expected_result

    # 获取实际结果值
    def get_result(self):
        return GlobalVar.result