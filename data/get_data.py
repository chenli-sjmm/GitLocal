#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: chenli
# project: SJMM

from test_data.heards import *
from test_data.domian import *
import json


class GetData:
    def __init__(self):
        self.opera_excel = OperationExcel()
        self.data_config = GlobalVar()

    # 获取表格行数，就是我们的case数量
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 获取是否执行
    def get_is_run(self, row):
        flag = None
        col = int(self.data_config.get_is_run())
        run_model = self.opera_excel.get_cell_value(row, col)
        if run_model == "yes":
            flag = True
        else:
            flag = False
        return flag

    # 获取heard
    def heard(self,row):
        col = int(self.data_config.get_heard())
        return self.opera_excel.get_cell_value(row, col)

    # 获取测试环境
    def domians(self, row):
        col = int(self.data_config.get_domian())
        return self.opera_excel.get_cell_value(row, col)

    # 获取url
    def get_urls(self,row):
        col = int(self.data_config.get_url())
        return self.opera_excel.get_cell_value(row, col)

    # 获取请求方式
    def gateway(self, row):
        col = int(self.data_config.get_gateway())
        return self.opera_excel.get_cell_value(row, col)

    # 获取请求body
    def get_body(self, row):
        col = int(self.data_config.get_body())
        str_body = self.opera_excel.get_cell_value(row, col)
        body = eval(str_body)
        return body

    def get_expect(self, row):
        col = int(self.data_config.get_expected_result())
        return self.opera_excel.get_cell_value(row, col)










if __name__ == '__main__':
    lien = GetData()
    print (lien.get_expect(1))


