# !/usr/bin/env python3
# !-*-coding:utf-8-*-

from pyemail import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
import os
import configparser
import time


class MyEmail:
    # 读取配置文件
    def __init__(self):
        # 读取文件绝对路径
        self.dir_path = os.path.dirname(os.path.abspath(__file__))
        self.config_file_path = self.dir_path + 'config/ini'
        cf = configparser.ConfigParser()
        cf.read(self.config_file_path, encoding='utf-8')
        COMMASPACE = ', '
        # 邮件发送服务器'smtp.exmail.qq.com'
        self.host = cf.get('email', 'mail_test')
        # 端口号
        self.port = cf.get('email', 'mail_port')
        # 邮箱账号
        self.user = cf.get('email', 'mail_user')
        # 邮箱密码
        self.password = cf.get('email', 'mail_pass')
        # 发件人
        self.sender = cf.get('email', 'mail_sender')
        # 收件人
        self.to = cf.get('email', 'mail_receiver').split(';')
        # 邮件抄送人
        self.cc = cf.get('email', 'mail_cc').split(';')

        #接收邮件总人数
        self.receiver = [x for x in self.to if x] + [x for x in self.cc if x]

        # 邮件标题
        self.subject = cf.get('email', 'subject')
        self.report_file = ''
        # 邮件内容
        self.content = cf.get('email', 'content')

        self.message = MIMEMultipart()
        self.message['From'] = self.sender
        self.message['To'] = COMMASPACE.join(self.to)
        self.message['Cc'] = COMMASPACE.join(self.cc)
        self.message['Subject'] = self.subject
        self.message['Date'] = formatdate()
        pass

    # 获取附件
    def get_attachment(self, report_dir=None):
        self.get_attach_file_name(report_dir)

        # 附件内容带附件正文
        with open(self.report_file, 'r', encoding='utf-8') as f:
            x = f.read()
            self.content += x
        # 构造附件
        with open(self.report_file, 'rb',) as f:
            attachment = MIMEText(f.read(), "base64", "utf-8")

        attachment["Content-Type"] = "application/octet-stream"
        filename = os.path.basename(self.report_file)

        # 附件名称为中文时的写法
        attachment.add_header("Content-Disposition", "attachment", filename=("gbk", "", filename))
        # 附件名称非中文时的写法
        # att["Content-Disposition"] = 'attachment; filename="test.html")'
        self.message.attach(attachment)
        return self

    # 获取文件名
    def get_attach_file_name(self, file_dir=None):
        if file_dir:
            report_dir = file_dir
        else:
            report_dir = self.dir_path + '/test_reports'

        if report_dir[-1] != '\\' and report_dir[-1] != '/':
            report_dir += "/"

        lists = os.listdir(report_dir)
        lists.sort(key=lambda fn: os.path.getctime(report_dir + fn))  # 按时间排序
        print(lists)
        # 先找到想要发送邮件的报告文件
        self.report_file = os.path.join(report_dir, lists[-1])
        return self.report_file

    # 发送邮件
    def send_mail(self):
        self.message.attach(MIMEText(self.content, 'html', 'utf-8'))
        if self.receiver == '':
            print("收件人为空，不发送邮件。请检查收件人和抄送人配置是否正确")
            return
        try:
            smtp = smtplib.SMTP_SSL(self.host, port=self.port)
            smtp.login(self.user, self.password)
            # 发送给多人、同时抄送给多人，发送人和抄送人放在同一个列表中
            smtp.sendmail(self.sender, self.receiver, self.message.as_string())
        except smtplib.SMTPException as e:
            print('error:', e)
        pass

if __name__ == '__main__':
    My = MyEmail()
    # 测试报告目录地址（相对路径）
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())  # 获取当前时间
    My.get_attachment('../RunDemo/report/' + now + '_test_result.html')
    My.send_mail()
