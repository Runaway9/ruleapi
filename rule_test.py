# -*- coding: utf-8 -*-
import requests
import json
import pytest
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
import allure

header = {'Content-Type': 'application/json'}
rule_xls = pd.read_excel(r'D:\规则引擎\测试案例\中韩1-120投保.xlsx', sheet_name='Sheet1')

"""
A function to test rules with various parameters and assertions.
"""
@pytest.mark.parametrize(
    "case_name, url, params, assertion, PassOrNot, cal_code",
    zip(rule_xls['case_name'], (rule_xls['url']), rule_xls['params'], (rule_xls['assertion']),
        (rule_xls['PassOrNot']), rule_xls['cal_code'])
)
def test_rule(case_name, url, params, assertion, PassOrNot, cal_code):
    for i in enumerate(str(params)):
        print('Excel测试用例编号', case_name)
        print('测试词条为', cal_code)
        sqlf = str(params).encode('utf-8')
        # 利安外网投保
        # info = requests.post(url='http://119.91.31.248:91/tbcont/validationTBContDetail', data=sqlf,
        #                       headers=header).text
        # 利安外网核保
        # info = requests.post(url='http://119.91.31.248:91/cont/validationContDetail', data=sqlf, headers=header).text
        # 中韩外网核保
        # info = requests.post(url='http://101.35.132.237/rule-actuator/cont/validationContDetail', data=sqlf,
        #                      headers=header).text
        # 中韩外网投保
        info = requests.post(url='http://101.35.132.237/rule-actuator/tbcont/validationTBContDetail', data=sqlf,
                             headers=header).text

        print('返回结果为：', info)
        object = json.loads(info)['data']['policyList']
        if PassOrNot == '规则被校验':
            if json.loads(info)['data']:
                if json.loads(info)['data']['policyList']:
                    if json.loads(info)['data']['policyList']:
                        my_list = ['']
                        for item in object:
                            my_list.append(item['ruleCode'])
                        try:
                            index = my_list.index(cal_code)
                        except ValueError:
                            index = -1
                        if index != -1:
                            print(cal_code, "有被校验，通过")
                            assert 1 == 1
                        else:
                            print(cal_code, "未被校验到，不通过")
                            assert 1 == 2
                        return
                else:
                    print(cal_code, '未被校验到，不通过')
                    assert 1 == 2
            else:
                print(cal_code, '未被校验到，不通过')
                assert 1 == 2
        elif PassOrNot == '规则不被校验':
            if json.loads(info)['data']:
                if json.loads(info)['data']['policyList']:
                    if json.loads(info)['data']['policyList']:
                        my_list = ['']
                        for item in object:
                            my_list.append(item['ruleCode'])
                        try:
                            index = my_list.index(cal_code)
                        except ValueError:
                            index = -1
                        if index != -1:
                            print(cal_code + "有被校验，不通过")
                            assert 1 == 2
                        else:
                            print(cal_code + "未被校验到，通过")
                            assert 1 == 1
                        return
                else:
                    print('预期结果：规则不被校验')
                    print('实际结果：规则不被校验')
                    assert 1 == 1
            else:
                print('预期结果：规则不被校验')
                print('实际结果：规则不被校验')
                assert 1 == 1
        break


# if __name__ == '__main__':
#     command_line = ["--alluredir=D:/AutoTest/rule/allure-results"]
#     pytest.main(command_line)
report_file = 'report.html'
pytest.main(['--html', report_file])

# allure报告
# pytest -sv scripts --alluredir=allure_data
# allure generate allure_data -o allure_report --clean

# # 邮件参数
# sender_email = 'secbreath@163.com'
# receiver_emails = ['936194582@qq.com', 'jiapeng@sinosoft.com.cn', '616007226@qq.com']
# subject = '测试案例'
# body = """
#     附件内容为python自动化脚本生成的测试案例，请查收！！
# """
# file_path = 'report.html'  # 你要发送的文件的路径
#
# # 创建一个MIMEMultipart对象
# message = MIMEMultipart()
# message['From'] = sender_email
# message['To'] = ', '.join(receiver_emails)
# message['Subject'] = subject  # 主题是纯文本，不需要使用Header包装
#
# # 添加正文
# message.attach(MIMEText(body, 'plain'))
#
# # 添加附件
# attachment = open(file_path, 'rb')
# part = MIMEBase('application', 'octet-stream')
# part.set_payload((attachment).read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', "attachment; filename= %s" % file_path)
# message.attach(part)
#
# # 邮件服务器设置
# smtp_server = 'smtp.163.com'  # 163邮箱的SMTP服务器地址
# smtp_port = 465  # 163邮箱的SMTP端口号
# smtp_username = 'secbreath@163.com'
# smtp_password = 'FKFRRUYOXJYJORIG'  # 生成的客户端授权码
#
# # 连接到SMTP服务器
# server = smtplib.SMTP_SSL(smtp_server, smtp_port)  # 使用SMTP_SSL()来使用SSL连接
# server.login(smtp_username, smtp_password)
#
# # 发送邮件
# server.sendmail(sender_email, receiver_emails, message.as_string())
#
# # 关闭SMTP连接
# server.quit()
#
# # 提示发送成功
# print('邮件发送成功')
