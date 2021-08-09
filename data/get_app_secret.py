#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: chenli
# project: SJMM

from test_data.get_data import *
class GetSecret:
    def __init__(self):
        self.data = GetData()

    def get_secret(self, row):
        environment = self.data.domians(row)
        if environment in ["APP_SIT", "APP_SIT02", 'APP_SIT03', 'APP_SIT04', 'APP_SIT05']:
            sit_secret = "4E725AB4DA67C24E09593B83B1E183DC"
            return sit_secret
        elif environment in ["APP_UAT", "APP_UAT02", 'APP_UAT03', 'APP_UAT04', 'APP_UAT05']:
            uat_secret = "DB21A2887C5579A99C4801C353E37C90"
            return uat_secret
        elif environment in ["APP_DEV", "APP_DEV02", 'APP_DEV03', 'APP_DEV04', 'APP_DEV05']:
            dev_secret = "12B654A77D9CDD37FBAEC6EA27981A3F"
            return dev_secret
        else:
            return environment








if __name__ == '__main__':
    a = GetSecret()
    print(a.get_secret(1))