#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: chenli
# project: SJMM

from function.operation_excel import OperationExcel
from test_data.data_config import *

class GetDomian:
    APP_SIT = "https://gateway-test.sjmama.com"
    APP_R_SIT = "https://gateway-ref-test.sjmama.com"
    APP_UAT = "https://gateway-uat.sjmama.com"
    APP_R_UAT = "https://gateway-ref-uat.sjmama.com"
    APP_SIT02 = "https://gateway-test02.sjmama.com"
    APP_SIT03 = "https://gateway-test03.sjmama.com"
    APP_SIT04 = "https://gateway-test04.sjmama.com"
    APP_SIT05 = "https://gateway-test05.sjmama.com"
    APP_UAT02 = "https://gateway-uat02.sjmama.com"
    APP_UAT03 = "https:/gateway-uat03.sjmama.com"
    APP_UAT04 = "https://gateway-uat04.sjmama.com"
    APP_UAT05 = "https://gateway-uat05.sjmama.com"
    def __init__(self,domian=None):
        self.opera_excel = OperationExcel()
        self.data_config = GlobalVar()
        self.domian = domian

    def get_domian(self,row):
        col = int(self.data_config.get_domian())
        domian = self.opera_excel.get_cell_value(row, col)
        if domian =="APP_SIT":
            return GetDomian.APP_SIT
        elif domian == "APP_R_SIT":
            return GetDomian.APP_R_SIT
        elif domian == "APP_UAT":
            return GetDomian.APP_UAT
        elif domian == "APP_R_UAT":
            return GetDomian.APP_R_UAT
        elif domian == "APP_SIT02":
            return GetDomian.APP_SIT02
        elif domian == "APP_SIT03":
            return GetDomian.APP_SIT03
        elif domian == "APP_SIT04":
            return GetDomian.APP_SIT04
        elif domian == "APP_SIT05":
            return GetDomian.APP_SIT05
        elif domian == "APP_UAT02":
            return GetDomian.APP_UAT02
        elif domian == "APP_UAT03":
            return GetDomian.APP_UAT03
        elif domian == "APP_UAT04":
            return GetDomian.APP_UAT04
        elif domian == "APP_UAT05":
            return GetDomian.APP_UAT05
        else:
            print("domian is error")



if __name__ == '__main__':
    d = GetDomian()
    print(d.get_domian(1))