#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: chenli
# project: SJMM


import json
import datetime
import requests

class GateWay:
    def post_main(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
        return res.json()

    def api_post(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
        return res.json()

        hearder = self.headers.get_heard(row)
        domain= self.domains.get_domian(row)
        sign = self.signs.get_sign(row)
        URI = self.urls.get_urls(row)
        body = json.dumps(self.urls.get_body(row))
        url = domain + URI + "?" + "sign=" + sign
        print(url)
        try:
            response = requests.request("POST", url, data=body, headers=hearder, verify=False)
        except BaseException:
            print(datetime.datetime.now().strftime('%Y%m%d %H:%M:%S.%f')[:-3] + URI + "：请求发生异常")
        return response



# import requests
# import json
# class RunMethod:
# 	def post_main(self,url,data,header=None):
# 		res = None
# 		if header !=None:
# 			res = requests.post(url=url,data=data,headers=header)
# 		else:
# 			res = requests.post(url=url,data=data)
# 		return res.json()
#
# 	def get_main(self,url,data=None,header=None):
# 		res = None
# 		if header !=None:
# 			res = requests.get(url=url,data=data,headers=header,verify=False)
# 		else:
# 			res = requests.get(url=url,data=data,verify=False)
# 		return res.json()
#
# 	def run_main(self,method,url,data=None,header=None):
# 		res = None
# 		if method == 'Post':
# 			res = self.post_main(url,data,header)
# 		else:
# 			res = self.get_main(url,data,header)
# 		return json.dumps(res,ensure_ascii=False)