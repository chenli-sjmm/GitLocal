#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: chenli
# project: SJMM

"""

1、url中必传参数：sign=xxxx,其中xxxx代表数据的签字值。

2、header必传参数：

Header Name	名称	说明
X-App-Id	AppId	此值是验证调用应用是否合法的必须标识，
由服务端授权AppId和AppSecret
X-Timestamp	时间戳	接口请求时刻的秒，
如：1552311967,调用端需要在合适的时间与服务端做时间同步校验。，
服务端会在每次请求响应中返回服务器的时间，，
如：X-Response-Server-Time=2019-03-11 21:48:09，
服务端会根据此时间来处理用户请求是否过期，超过指定的时长将拒绝服务。
X-Uniquely-Code	唯一码	一般为移动设置的机器唯一码
X-Nonce	唯一请求标识	每次请求都必须重新生成一个全服唯一码，避免用户进行恶意重复请求。
建议唯一码使用UUID。
X-Client-Type	客户端类型	ios=苹果、android=安卓、web=Web网站、weixin=微信、other=其它
X-App-Type	App类型	app_business=商户版、app_user=用户版、app_all_user=综合版
X-Auth-Token	登录token	用户登录后的token，建议所有接口都传此参数，
未登录的用户传空格即可，如：X-Auth-Token=""，header中必须要有此项。


签名算法

1、requestUri：先将请求接口地址去除前面的域名，比如：http://localhost:9000/sjmm-mall/api/demos/list,只保留：/sjmm-mall/api/demos/list作为签名字符串的第一部分。

2、headerData:将上面header中的必传参数，按表格顺序将值使用"."号连接，空值(非null)也必须使用"."连接。 比如：

X-App-Id.X-Timestamp.X-Uniquely-Code.X-Nonce.X-Client-Type.X-App-Type.X-Auth-Token
如果其中X-App-Type值为空，也要连接在字符串中。

X-App-Id.X-Timestamp.X-Uniquely-Code.X-Nonce.X-Client-Type..X-Auth-Token
3、queryData：请url中除sign以外的参数键值对取出，按字典顺序排序并连接起来。比如：请求参数是

pageNumber=4&pageSize=3&sign=b9e8a8405f0718abe463e99d4d683401&name=x&mobile=xx
取出并排序连接后为：mobile=xxname=xpageNumber=4pageSize=3

4、bodyData：对于post请求的body数据为json格式，必须按请求传入格式一模一样进行签名。比如：

{
    "name": "刘久武2",
    "password": "123456",
    "mobile":"13826526941"
}
该格式中换行符、空格都不参少，建议调用客户端将此json格式化成一行并去掉多余的空格传输，以勉签名校验失败。即：

{"name":"刘久武2","password":"123456","mobile":"13826526941"}
最终的签名字符串组成：

appSecret.requestUri.headerData.queryData.bodyData
将上面的字符串进行URLEncoder编码后，再使用MD5加密通过sign参数传给接口即可。

重要提醒： 其中appSecret的值是绝对保密的，应用调用端一定要保护好，不可泄漏

最后完整的请求地址类似如下：

http://xxx/sjmm-mall/api/demos/list?pageNumber=4&pageSize=3&sign=b9e8a8405f0718abe463e99d4d683401&name=x&mobile=xx
header参数：

X-App-Id:123456
X-Timestamp:1552276092
X-Uniquely-Code:sss2
X-Nonce:333223
X-Client-Type:android
X-App-Type:app_user
X-Auth-Token:234324efsfsf
Content-Type:application/json
"""
import json
import datetime
import requests
from test_data.get_sign import GetSign
from test_data.get_data import GetHeards
from test_data.domian import GetDomian
from test_data.get_data import GetData


class GateWay:
    def __init__(self):
        self.signs = GetSign()
        self.headers = GetHeards()
        self.domains = GetDomian()
        self.urls = GetData()

    def api_post(self,row):
        hearder = self.headers.get_heard(row)
        domain= self.domains.get_domian(row)
        sign = self.signs.post_sign(row)
        URI = self.urls.get_urls(row)
        body = json.dumps(self.urls.get_body(row))
        url = domain + URI + "?" + "sign=" + sign
        print(url)
        try:
            response = requests.request("POST", url, data=body, headers=hearder, verify=False)
        except BaseException:
            print(datetime.datetime.now().strftime('%Y%m%d %H:%M:%S.%f')[:-3] + URI + "：请求发生异常")
        return response

    def api_get(self,row):
        hearder = self.headers.get_heard(row)
        domain = self.domains.get_domian(row)
        sign = self.signs.get_sign(row)
        URI = self.urls.get_urls(row)
        body = json.dumps(self.urls.get_body(row))
        query = []
        queryData_Uri = ''
        if body != '':
            for i in body.keys():
                query.append(i)
        query.sort()
        for i in query:
            queryData_Uri += i + '=' + str(body[i]) + '&'
        url = domain + URI + "?" + queryData_Uri + "sign=" + sign
        print(url)
        try:
            response = requests.request('get', url, data='', headers=hearder, verify=False)
        except BaseException:
            print(datetime.datetime.now().strftime('%Y%m%d %H:%M:%S.%f')[:-3] + URI + "：请求发生异常")
        return response


    def api_request_main(self, row):
        request_method = self.urls.gateway(row)
        if request_method == "post":
            res = self.api_post(row)
            return res.json()
        elif request_method == "get":
            res = self.api_get(row)
            return res.json()
        else:
            return request_method





if __name__ == '__main__':
    a = GateWay()
    print(a.api_request_main(1))

