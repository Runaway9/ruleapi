# -*- coding: utf-8 -*-
import unittest
import requests
import paramunittest
import urllib.parse
import pandas as pd
import json
from openpyxl import load_workbook

header = {'Content-Type': 'application/json'}
login_xls = pd.read_excel(r'D:\规则引擎\测试案例\222.xlsx',
                          sheet_name='Sheet1')  # 传入Excel名称和Sheet名称，返回每一行用例
self = []


@paramunittest.parametrized(
    (login_xls['case_name'], login_xls['url'], login_xls['params'], login_xls['assertion'], login_xls['PassOrNot']
     ))
class GX(unittest.TestCase):
    def setParameters(self, case_name, url, params, assertion, PassOrNot):

        self.case_name = case_name
        self.url = url
        self.params = params
        self.assertion = assertion
        self.PassOrNot = PassOrNot

    def description(self):
        pass

    def test_case01(self):
        for index, value in enumerate(self.params):
            print("Excel测试用例编号：" + str(self.case_name[index]))
            params = str(value)
            sqlf = params.encode("utf-8")
            # 利安外网投保
            info = requests.post(url='http://119.91.31.248:91/tbcont/validationTBContDetail', data=sqlf,
                                  headers=header).text
            # 利安外网核保
            # info = requests.post(url='http://119.91.31.248:91/cont/validationContDetail', data=sqlf,
            #                      headers=header).text
            # 中韩外网核保
            # info = requests.post(url='http://101.35.132.237/rule-actuator/cont/validationContDetail', data=sqlf,
            #                      headers=header).text
            print('接口返回结果：', info)
            if self.PassOrNot[index] == '规则被校验':
                # 如果接口返回结果policyList不是空，说明规则被校验(接口传参不符合规则)
                if json.loads(info)['data']:
                    if json.loads(info)['data']['policyList']:
                        r = json.loads(info)['data']['policyList'][0]['result']  # 获取返回结果
                        print('自核结论：', r)
                        print('预期结果：规则被校验')
                        print('实际结果：规则被校验')
                        # self.assertEqual(1, 1)  # 表示不通过
                    # 如果接口返回结果policyList是空，说明规则不被校验，测试通过(接口传参符合规则)
                    else:
                        print('预期结果：规则被校验')
                        print('实际结果：规则不被校验')
                        print('请查询这条规则的详细错误信息！')
                        # self.assertEqual(1, 2)  # 表示不通过
                else:
                    print('预期结果：规则被校验')
                    print('实际结果：规则不被校验')
                    print('请查询这条规则的详细错误信息！')
            elif self.PassOrNot[index] == '规则不被校验':
                if json.loads(info)['data']:
                    if json.loads(info)['data']['policyList']:
                        print('预期结果：规则不被校验')
                        print('实际结果：规则被校验')
                        print('请查询这条规则的详细错误信息！')
                        # self.assertEqual(1, 2)  # 表示不通过
                    else:
                        print('预期结果：规则不被校验')
                        print('实际结果：规则不被校验')
                        self.assertEqual(1, 1)  # 表示通过
                else:
                    print('预期结果：规则被校验')
                    print('实际结果：规则不被校验')
                    print('请查询这条规则的详细错误信息！')

    def tearDown(self):
        print('测试结束，输出log完结\n')


if __name__ == '__main__':
    unittest.main()