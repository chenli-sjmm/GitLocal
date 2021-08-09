#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: chenli
# project: SJMM

import json
from function.new_gateway import *
class CommonUtil:
	def is_contain(self,str_one,str_two):
		'''
		判断一个字符串是否再另外一个字符串中
		str_one:查找的字符串
		str_two：被查找的字符串
		'''


		# flag = None
		# if isinstance(str_one, unicode):
		# 	str_one = str_one.encode('unicode-escape').decode('string_escape')
		if str_one in str_two:
			print("测试通过")
			# flag = True
		else:
			return str_two




	def is_equal_dict(self,dict_one,dict_two):
		'''
		判断两个字典是否相等
		'''
		if isinstance(dict_one,str):
			dict_one = json.loads(dict_one)
		if isinstance(dict_two,str):
			dict_two = json.loads(dict_two)


if __name__ == '__main__':
	str1 = GateWay().api_request_main(1)
	print(str1)
	str2 = GetData().get_expect(1)
	print(str2)
	a= CommonUtil().is_contain(str2,str1)
	print(a)