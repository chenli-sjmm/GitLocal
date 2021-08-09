import unittest
from test_case import web_login
from test_case import LoginAPP
import HTMLTestRunner
'''
# 通过文件夹获取所有符合条件的用例
dis = unittest.defaultTestLoader.discover("E:\\sjmm_automation\\test_case", "web_login.py")
# 创建一个测试用例套件，并放入测试用例集
suite = unittest.TestSuite(dis)
# 运行所创建的测试套件
unittest.TextTestRunner().run(suite)
'''

testunit= unittest.TestSuite()

testunit.addTest(web_login.loginTestCase("testlogin"))
testunit.addTest(LoginAPP.MyTestCase("testLuncherAPP"))

runner=unittest.TextTestRunner()
file = open("E:\\sjmm_automation\\report\\test1.htm2", "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=file, title=u"用例管理",description=u"用例测试情况")
runner.run(testunit)