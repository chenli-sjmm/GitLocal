#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:chen_li
# project: SJMM

import xlrd


class ReadExcel:
    def __init__(self, file_path):
        try:
            self.book = xlrd.open_workbook(file_path)
        except:
            print('No File %s' % file_path)
        self.sheet_names = self.book.sheet_names()
        self.sheet_num = self.book.nsheets
        self.sheet = self.book.sheet_by_index(0)
        self.row_num = self.sheet.nrows
        self.col_num = self.sheet.ncols

    def read_sheet_name(self, sheet_name):
        try:
            self.sheet = self.book.sheet_by_name(sheet_name)
        except:
            print("No Sheet %s" % sheet_name)
        # 获取行数列数
        self.row_num = self.sheet.nrows
        self.col_num = self.sheet.ncols

    def read_sheet_index(self, sheet_index):
        try:
            self.sheet = self.book.sheet_by_index(sheet_index)
        except:
            print("No Sheet Index %s" % sheet_index)
        # 获取行数列数
        self.row_num = self.sheet.nrows
        self.col_num = self.sheet.ncols

    def get_sheet_names(self):
        return self.sheet_names

    # 读取单元格内容
    def get_cell_value(self, row, col):
        return self.sheet.cell_value(row, col)

    # 读取某行数据
    def get_row_data(self, row):
        return self.sheet.row_values(row)

    # 读取某列数据
    def get_col_data(self, col):
        return self.sheet.col_values(col)

    # 读取所有行数据
    def get_sheet_rows_data(self):
        data = []
        for i in range(0, self.row_num):
            row_value_list = self.sheet.row_values(i)
            data.append(row_value_list)
        return data

    # 读取所有列数据
    def get_sheet_cols_data(self):
        data = []
        for i in range(0, self.col_num):
            col_value_list = self.sheet.col_values(i)
            data.append(col_value_list)
        return data

    # 读取所有sheet行数据
    def get_file_rows_data(self):
        data = []
        for name in self.sheet_names:
            self.read_sheet_name(name)
            sheet_data = self.get_sheet_rows_data()
            sheet_data.append(['SheetName', name])
            data.append(sheet_data)
        return data

    # 读取所有sheet列数据
    def get_file_cols_data(self):
        data = []
        for i in range(0, self.sheet_num):
            self.read_sheet_index(i)
            data.append(self.get_sheet_cols_data())
        return data

    # 读取指定列的行数据
    def get_choose_rows_data(self, start_index, end_index):
        data = []
        for i in range(1, self.row_num):
            row_value_list = self.sheet.row_values(i, start_index, end_index)
            data.append(row_value_list)
        return data

    # 读取指定列关键字的行数据
    def get_keys_rows_data(self, keys):
        data = []
        keys_value = self.sheet.row_values(0)
        key_indexes = []
        for key_index in range(0, len(keys)):
            for index in range(0, len(keys_value)):
                if keys_value[index] == keys[key_index]:
                    key_indexes.append(index)
        for j in range(1, self.row_num):
            row_value_list = []
            for i in range(0, len(key_indexes)):
                row_value_list.append(self.sheet.cell_value(j, key_indexes[i]))
            data.append(row_value_list)
        return data
