import json
import pymysql
import pandas as pd
import datetime

res = []  # 最终返回的列表
reslist = []


def get_mysql(cal_code3, sale_chnl3, sell_type3, riskStyle3):
    bom01 = {
    "batchCount": None,
    "batchNo": None,
    "batchNum": None,
    "bnfList": [
        {
            "bnfGrade": "1",
            "bnfNo": 100000,
            "bnfType": 0.0,
            "idexpDate": 253402185600000,
            "idno": "330281198710194180",
            "idtype": "A",
            "insuredNo": "253402185600000",
            "nativePlace": "CHN",
            "relationtoInsured": "1",
            "rgtAddress": "户口所在地",
            "sex": "1"
        }
    ],
    "bomAgent": {
        "agentCode": "6601300024",
        "agentState": "04",
        "blacklisFlag": "A",
        "branchType": "3",
        "outWorkDate": 1582905600000
    },
    "bomAppnt": {
        "address": "杭州",
        "appntAge": 16,
        "avoirdupois": 70,
        "companyPhone": "公司电话",
        "email": "342304792@qq.com",
        "homePhone": "固定电话",
        "idexpDate": 253402185600000,
        "idno": "330281198710194180",
        "idtype": "0",
        "mobile": "15958811700",
        "nativePlace": "CHN",
        "occupationCode": "0103002",
        "occupationType": "1",
        "personalProve": "1",
        "postalAddress": "浙江省宁波市",
        "relationtoInsured": "00",
        "rgtAddress": "户口所在地",
        "sameAddessPNum": 0,
        "sex": "1",
        "stature": 178,
        "taxType": "税收居民类型",
        "yearIncome": 0.0
    },
    "bomGrpCustomer": None,
    "bomGrpPolicy": None,
    "bomPolicy": {
        "Amnt": 0.0,
        "agentCom": "0601010079",
        "agentType": "3",
        "contNo": "2018060402000013",
        "forceUWFlag": "0",
        "lowestOneYearPrem": 0,
        "oneMSumDangerAmnt": "-1",
        "payIntv": 0,
        "polApplyDate": 1528041600000,
        "prem": 0.0,
        "saleChnl": "04",
        "sellType": "01"
    },
    "bussiType": "TB",
    "contNo": "2022111401000003",
    "dutyList": None,
    "grpContNo": "00000000000000000000",
    "grpPolList": [
        {
            "amnt": 0.0,
            "bonusFlag": "1",
            "bonusGetMode": "2",
            "insuYear": 1,
            "insuYearFlag": "Y",
            "payEndYearFlag": "Y",
            "payIntv": 0,
            "payYears": 0,
            "prem": 0.0,
            "riskCode": "211601",
            "riskPeroid": "L",
            "rnewFlag": "1"
        }
    ],
    "immediateinventorydataAppnt": None,
    "immediateinventorydataInsu": None,
    "inputOperator": "ybt",
    "insuredList": [
        {
            "address": "被保人地址",
            "avoirdupois": 70,
            "birthDay": 561571200000,
            "companyPhone": "公司电话",
            "homePhone": "固定电话",
            "idexpDate": 253402185600000,
            "idno": "330281198710194180",
            "idtype": "0",
            "insuredNo": "253402185600000",
			"insuredAge": "16",
            "lfsumDangerAmnt42": "12000001",
            "mobile": "15958811700",
            "nativePlace": "CHN",
            "occupationCode": "0103002",
            "occupationType": "1",
            "polApplyDate": 1528041600000,
            "postalAddress": "浙江省宁波市",
            "preferredPhone": "首选电话",
            "qualityState": None,
            "relationToAppnt": "00",
            "rgtAddress": "户口所在地",
            "riskCount1066005": 0,
            "sameAddessPNum": 0,
            "sex": "1",
            "stature": 178,
            "taxType": "税收居民类型",
            "yearIncome": 0.0,
            "yearIncome10": 0.0,
            "yearIncome15": 0.0,
            "yearIncome20": 0.0,
            "yearIncome8": 0.0
        }
    ],
    "mainPolList": [
        {
            "amnt": 0.0,
            "bonusFlag": "1",
            "bonusGetMode": "2",
            "insuYear": 10,
            "insuYearFlag": "Y",
            "insuredNo": "253402185600000",
            "mainPolNo": "",
            "payEndYearFlag": "Y",
            "payIntv": 0,
            "payYears": 0,
            "prem": 0.0,
            "riskCode": "121504",
            "riskPeroid": "L",
            "riskStyle": None,
            "rnewFlag": "1"
        }
    ],
    "policyList": None,
    "ruleFlag": "A",
    "saleChnl": "04",
    "sellType": "01",
    "subPolList": [
        {
            "amnt": 0.0,
            "contPlanCode": "保险计划编码",
            "insuYear": 1,
            "insuYearFlag": "Y",
            "insuredNo": "253402185600000",
            "mainPolNo": "",
            "payEndYearFlag": "Y",
            "payIntv": 0,
            "payYears": 0,
            "prem": 0.0,
            "riskCode": "211601",
            "riskPeroid": "L",
            "rnewFlag": "1"
        }
    ],
    "ybtContNo": None
}
    # 保单

    # 销售人员

    # 被保人
    insuredList = json.dumps(bom01["insuredList"][0])
    insuredList02 = json.loads(insuredList)
    # 主险
    mainPolList = json.dumps(bom01["mainPolList"][0])
    mainPolList02 = json.loads(mainPolList)
    # 险种
    bomPolicy = json.dumps(bom01["bomPolicy"])
    bomPolicy02 = json.loads(bomPolicy)
    # 投保人
    bomAppnt = json.dumps(bom01["bomAppnt"])
    bomAppnt02 = json.loads(bomAppnt)
    # 受益人
    bnfList = json.dumps(bom01["bnfList"][0])
    bnfList02 = json.loads(bnfList)
    # 附加险
    subPolList = json.dumps(bom01["subPolList"][0])
    subPolList02 = json.loads(subPolList)
    # 服务人员
    bomAgent = json.dumps(bom01["bomAgent"])
    bomAgent02 = json.loads(bomAgent)

    # 打开数据库连接
    # 利安外网
    # db = pymysql.connect(host="119.91.31.248", port=13306, user="root", password="chenchenchen", database="lian_dat_ww",
    #                      cursorclass=pymysql.cursors.DictCursor)
    # 中韩外网
    db = pymysql.connect(host="101.35.132.237", port=13306, user="root", password="1qaz@WSXcode", database="dc_rule",
                         cursorclass=pymysql.cursors.DictCursor)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = """
     SELECT
        li.DECISION_CODE,
        li.SPLICING,
        li.OBJECT_CODE,
        li.ENTRY_CODE,
        li.OPERATION_CODE,
        lr.RESULTSET,
        li.ENTRY_INFORMATION,
        lr.RULE_RESULT,
        lm.RULE_GROUP,
        lm.CAL_CODE
     FROM
        lrruledecisioninformat li,
        lrruledecisionresult lr,
        lrruleinformation lm
     WHERE li.DECISION_CODE = lr.DECISION_CODE
     AND li.CAL_CODE = lm.CAL_CODE
     AND li.CAL_CODE = %s
     ORDER BY lr.DECISION_CODE
"""

    # 执行SQL语句
    cursor.execute(sql, [cal_code3])
    # 获取所有记录列表
    results = cursor.fetchall()
    resu_ocode_ecode_ei = []

    for row in results:
        print(row)
        decision_code = row['DECISION_CODE']
        splicing = row['SPLICING']
        object_code = row['OBJECT_CODE']
        entry_code = row['ENTRY_CODE']  # 接口要传的字段
        operation_code = row['OPERATION_CODE']  # 参数和参数值之间的运算符
        resultset = row['RESULTSET']  # 接口要传的参数值
        entry_information = row['ENTRY_INFORMATION']
        rule_result = row['RULE_RESULT']
        rule_group = row['RULE_GROUP']  # 险种编码

        resu_ocode_ecode_ei.append(object_code + "." + entry_code + ":" + entry_information)
        # 将接口字段首字母转为小写(包括与首字母相连的大写字母)
        entry_code02 = ""
        c = 0
        for i in range(len(entry_code)):
            a = entry_code[i]
            if a.isupper() and (c == 0):
                b = str.lower(a)
                entry_code02 += b
            else:
                c += 1
                entry_code02 += a

        # 被保人
        if object_code == "BomInsured":
            resultset03 = 0
            if operation_code == ">" or operation_code == ">=":
                try:
                    resultset02 = int(resultset)
                    resultset02 += 1
                    resultset03 = str(resultset02)
                except ValueError:
                    resultset00 = resultset.split(".")
                    resultset000 = int(resultset00[0]) + 1
                    resultset03 = str(resultset000)
            elif operation_code == "<" or operation_code == "<=":
                try:
                    resultset02 = int(resultset)
                    resultset02 -= 1
                    resultset03 = str(resultset02)
                except ValueError:
                    resultset00 = resultset.split(".")
                    resultset000 = int(resultset00[0]) - 1
                    resultset03 = str(resultset000)
            elif operation_code == "in":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0])
            elif operation_code == "!in":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0] + "1")  # 待完善
            elif operation_code == "!=":
                resultset03 = str(resultset + "1")  # 待完善
            elif operation_code == "==":
                resultset03 = str(resultset)
            elif operation_code == "strEquals":
                resultset03 = str(resultset)
            elif operation_code == "!strEquals":
                if entry_code == "Name":
                    resultset0 = str(resultset)
                    resultset00 = resultset0[0:-1]
                    resultset03 = resultset00
                else:
                    resultset03 = str(resultset) + "1"
            elif operation_code == "None":
                resultset03 = None
            elif operation_code == "!None":
                resultset03 = resultset
            elif operation_code == "!include":
                resultset0 = resultset[0]
                resultset00 = resultset0 + "1"
                resultset000 = resultset[1:]
                resultset03 = resultset00 + resultset000
            elif operation_code == "include":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0])
            elif operation_code == "!mod":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 + resultset01 + 1
                resultset03 = str(resultset01_1)
            elif operation_code == "mod":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 * resultset01
                resultset03 = str(resultset01_1)
            elif operation_code == "startsWith":
                resultset03 = str(resultset)
            elif operation_code == "length_less":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            elif operation_code == "chinese_length_less":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            elif operation_code == "!length":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            elif operation_code == "notRegex":
                resultset03 = str(resultset + 'a')
            elif operation_code == "length_big":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 + 1
                resultset03 = str(resultset01_1)
            elif operation_code == "to_yyyy":
                resultset03 = str(resultset)
            elif operation_code == "floatPart":
                resultset03 = str(resultset)
            elif operation_code == "to_mm":
                resultset03 = str(resultset)
            elif operation_code == "floor":
                resultset03 = str(resultset)
            elif operation_code == "to_dd":
                resultset03 = str(resultset)
            elif operation_code == "regex":
                resultset03 = str(resultset)
            elif operation_code == "endsWith":
                resultset03 = str(resultset)
            elif operation_code == "length":
                resultset03 = str(resultset)
            # 给insuredList02字典的entry_code02字段赋resultset02值
            insuredList02[entry_code02] = resultset03
            bom01["insuredList"] = [insuredList02]

        # 主险
        elif object_code == "BomMainPol":
            resultset03 = 0
            if operation_code == ">" or operation_code == ">=":
                try:
                    resultset02 = int(resultset)
                    resultset02 += 1
                    resultset03 = str(resultset02)
                except ValueError:
                    resultset00 = resultset.split(".")
                    resultset000 = int(resultset00[0]) + 1
                    resultset03 = str(resultset000)
            elif operation_code == "<" or operation_code == "<=":
                try:
                    resultset02 = int(resultset)
                    resultset02 -= 1
                    resultset03 = str(resultset02)
                except ValueError:
                    resultset00 = resultset.split(".")
                    resultset000 = int(resultset00[0]) - 1
                    resultset03 = str(resultset000)
            elif operation_code == "in":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0])
            elif operation_code == "!in":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0] + "1")  # 待完善
            elif operation_code == "!=":
                resultset03 = str(resultset + "1")  # 待完善
            elif operation_code == "==":
                resultset03 = str(resultset)
            elif operation_code == "strEquals":
                resultset03 = str(resultset)
            elif operation_code == "!strEquals":
                if entry_code == "Name":
                    resultset0 = str(resultset)
                    resultset00 = resultset0[0:-1]
                    resultset03 = resultset00
                else:
                    resultset03 = str(resultset) + "1"
            elif operation_code == "None":
                resultset03 = None
            elif operation_code == "!None":
                resultset03 = resultset
            elif operation_code == "!include":
                resultset0 = resultset[0]
                resultset00 = resultset0 + "1"
                resultset000 = resultset[1:]
                resultset03 = resultset00 + resultset000
            elif operation_code == "include":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0])
            elif operation_code == "!mod":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 + resultset01 + 1
                resultset03 = str(resultset01_1)
            elif operation_code == "mod":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 * resultset01
                resultset03 = str(resultset01_1)
            elif operation_code == "startsWith":
                resultset03 = str(resultset)
            elif operation_code == "length_less":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            elif operation_code == "chinese_length_less":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            elif operation_code == "!length":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            elif operation_code == "notRegex":
                resultset03 = str(resultset + 'a')
            elif operation_code == "length_big":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 + 1
                resultset03 = str(resultset01_1)
            elif operation_code == "to_yyyy":
                resultset03 = str(resultset)
            elif operation_code == "floatPart":
                resultset03 = str(resultset)
            elif operation_code == "to_mm":
                resultset03 = str(resultset)
            elif operation_code == "floor":
                resultset03 = str(resultset)
            elif operation_code == "to_dd":
                resultset03 = str(resultset)
            elif operation_code == "regex":
                resultset03 = str(resultset)
            elif operation_code == "endsWith":
                resultset03 = str(resultset)
            elif operation_code == "length":
                resultset03 = str(resultset)
                # 给insuredList02字典的entry_code02字段赋resultset02值
            mainPolList02[entry_code02] = resultset03
            bom01["mainPolList"] = [mainPolList02]

        # 保单
        elif object_code == "BomPolicy":
            resultset03 = 0
            if operation_code == ">" or operation_code == ">=":
                try:
                    resultset02 = int(resultset)
                    resultset02 += 1
                    resultset03 = str(resultset02)
                except ValueError:
                    resultset00 = resultset.split(".")
                    resultset000 = int(resultset00[0]) + 1
                    resultset03 = str(resultset000)
            elif operation_code == "<" or operation_code == "<=":
                try:
                    resultset02 = int(resultset)
                    resultset02 -= 1
                    resultset03 = str(resultset02)
                except ValueError:
                    resultset00 = resultset.split(".")
                    resultset000 = int(resultset00[0]) - 1
                    resultset03 = str(resultset000)
            elif operation_code == "in":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0])
            elif operation_code == "!in":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0] + "1")  # 待完善
            elif operation_code == "!=":
                resultset03 = str(resultset + "1")  # 待完善
            elif operation_code == "==":
                resultset03 = str(resultset)
            elif operation_code == "strEquals":
                resultset03 = str(resultset)
            elif operation_code == "!strEquals":
                if entry_code == "Name":
                    resultset0 = str(resultset)
                    resultset00 = resultset0[0:-1]
                    resultset03 = resultset00
                else:
                    resultset03 = str(resultset) + "1"
            elif operation_code == "None":
                resultset03 = None
            elif operation_code == "!None":
                resultset03 = resultset
            elif operation_code == "!include":
                resultset0 = resultset[0]
                resultset00 = resultset0 + "1"
                resultset000 = resultset[1:]
                resultset03 = resultset00 + resultset000
            elif operation_code == "include":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0])
            elif operation_code == "!mod":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 + resultset01 + 1
                resultset03 = str(resultset01_1)
            elif operation_code == "mod":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 * resultset01
                resultset03 = str(resultset01_1)
            elif operation_code == "startsWith":
                resultset03 = str(resultset)
            elif operation_code == "length_less":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            elif operation_code == "chinese_length_less":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            elif operation_code == "!length":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            elif operation_code == "notRegex":
                resultset03 = str(resultset + 'a')
            elif operation_code == "length_big":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 + 1
                resultset03 = str(resultset01_1)
            elif operation_code == "to_yyyy":
                resultset03 = str(resultset)
            elif operation_code == "floatPart":
                resultset03 = str(resultset)
            elif operation_code == "to_mm":
                resultset03 = str(resultset)
            elif operation_code == "floor":
                resultset03 = str(resultset)
            elif operation_code == "to_dd":
                resultset03 = str(resultset)
            elif operation_code == "regex":
                resultset03 = str(resultset)
            elif operation_code == "endsWith":
                resultset03 = str(resultset)
            elif operation_code == "length":
                resultset03 = str(resultset)
            # 给insuredList02字典的entry_code02字段赋resultset02值
            bomPolicy02[entry_code02] = resultset03
            bom01["bomPolicy"] = bomPolicy02

        # 投保人
        elif object_code == "BomAppnt":
            resultset03 = 0
            if operation_code == ">" or operation_code == ">=":
                try:
                    resultset02 = int(resultset)
                    resultset02 += 1
                    resultset03 = str(resultset02)
                except ValueError:
                    resultset00 = resultset.split(".")
                    resultset000 = int(resultset00[0]) + 1
                    resultset03 = str(resultset000)
            elif operation_code == "<" or operation_code == "<=":
                try:
                    resultset02 = int(resultset)
                    resultset02 -= 1
                    resultset03 = str(resultset02)
                except ValueError:
                    resultset00 = resultset.split(".")
                    resultset000 = int(resultset00[0]) - 1
                    resultset03 = str(resultset000)
            elif operation_code == "in":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0])
            elif operation_code == "!in":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0] + "1")  # 待完善
            elif operation_code == "!=":
                resultset03 = str(resultset + "1")  # 待完善
            elif operation_code == "==":
                resultset03 = str(resultset)
            elif operation_code == "strEquals":
                resultset03 = str(resultset)
            elif operation_code == "!strEquals":
                if entry_code == "Name":
                    resultset0 = str(resultset)
                    resultset00 = resultset0[0:-1]
                    resultset03 = resultset00
                else:
                    resultset03 = str(resultset) + "1"
            elif operation_code == "None":
                resultset03 = None
            elif operation_code == "!None":
                resultset03 = resultset
            elif operation_code == "!include":
                resultset0 = resultset[0]
                resultset00 = resultset0 + "1"
                resultset000 = resultset[1:]
                resultset03 = resultset00 + resultset000
            elif operation_code == "include":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0])
            elif operation_code == "!mod":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 + resultset01 + 1
                resultset03 = str(resultset01_1)
            elif operation_code == "mod":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 * resultset01
                resultset03 = str(resultset01_1)
            elif operation_code == "startsWith":
                resultset03 = str(resultset)
            elif operation_code == "length_less":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            elif operation_code == "chinese_length_less":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            elif operation_code == "!length":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            elif operation_code == "notRegex":
                resultset03 = str(resultset + 'a')
            elif operation_code == "length_big":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 + 1
                resultset03 = str(resultset01_1)
            elif operation_code == "to_yyyy":
                resultset03 = str(resultset)
            elif operation_code == "floatPart":
                resultset03 = str(resultset)
            elif operation_code == "to_mm":
                resultset03 = str(resultset)
            elif operation_code == "floor":
                resultset03 = str(resultset)
            elif operation_code == "to_dd":
                resultset03 = str(resultset)
            elif operation_code == "regex":
                resultset03 = str(resultset)
            elif operation_code == "endsWith":
                resultset03 = str(resultset)
            elif operation_code == "length":
                resultset03 = str(resultset)
            # 给insuredList02字典的entry_code02字段赋resultset02值
            bomAppnt02[entry_code02] = resultset03
            bom01["bomAppnt"] = bomAppnt02

        # 受益人
        elif object_code == "BomBnf":
            resultset03 = 0
            if operation_code == ">" or operation_code == ">=":
                try:
                    resultset02 = int(resultset)
                    resultset02 += 1
                    resultset03 = str(resultset02)
                except ValueError:
                    resultset00 = resultset.split(".")
                    resultset000 = int(resultset00[0]) + 1
                    resultset03 = str(resultset000)
            elif operation_code == "<" or operation_code == "<=":
                try:
                    resultset02 = int(resultset)
                    resultset02 -= 1
                    resultset03 = str(resultset02)
                except ValueError:
                    resultset00 = resultset.split(".")
                    resultset000 = int(resultset00[0]) - 1
                    resultset03 = str(resultset000)
            elif operation_code == "in":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0])
            elif operation_code == "!in":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0] + "1")  # 待完善
            elif operation_code == "!=":
                resultset03 = str(resultset + "1")  # 待完善
            elif operation_code == "==":
                resultset03 = str(resultset)
            elif operation_code == "strEquals":
                resultset03 = str(resultset)
            elif operation_code == "!strEquals":
                if entry_code == "Name":
                    resultset0 = str(resultset)
                    resultset00 = resultset0[0:-1]
                    resultset03 = resultset00
                else:
                    resultset03 = str(resultset) + "1"
            elif operation_code == "None":
                resultset03 = None
            elif operation_code == "!None":
                resultset03 = resultset
            elif operation_code == "!include":
                resultset0 = resultset[0]
                resultset00 = resultset0 + "1"
                resultset000 = resultset[1:]
                resultset03 = resultset00 + resultset000
            elif operation_code == "include":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0])
            elif operation_code == "!mod":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 + resultset01 + 1
                resultset03 = str(resultset01_1)
            elif operation_code == "mod":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 * resultset01
                resultset03 = str(resultset01_1)
            elif operation_code == "startsWith":
                resultset03 = str(resultset)
            elif operation_code == "length_less":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            elif operation_code == "chinese_length_less":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            elif operation_code == "!length":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            elif operation_code == "notRegex":
                resultset03 = str(resultset + 'a')
            elif operation_code == "length_big":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 + 1
                resultset03 = str(resultset01_1)
            elif operation_code == "to_yyyy":
                resultset03 = str(resultset)
            elif operation_code == "floatPart":
                resultset03 = str(resultset)
            elif operation_code == "to_mm":
                resultset03 = str(resultset)
            elif operation_code == "floor":
                resultset03 = str(resultset)
            elif operation_code == "to_dd":
                resultset03 = str(resultset)
            elif operation_code == "regex":
                resultset03 = str(resultset)
            elif operation_code == "endsWith":
                resultset03 = str(resultset)
            elif operation_code == "length":
                resultset03 = str(resultset)
            # 给insuredList02字典的entry_code02字段赋resultset02值
            bnfList02[entry_code02] = resultset03
            bom01["bnfList"] = [bnfList02]

        # 附加险
        elif object_code == "BomSubPol":
            resultset03 = 0
            if operation_code == ">" or operation_code == ">=":
                try:
                    resultset02 = int(resultset)
                    resultset02 += 1
                    resultset03 = str(resultset02)
                except ValueError:
                    resultset00 = resultset.split(".")
                    resultset000 = int(resultset00[0]) + 1
                    resultset03 = str(resultset000)
            elif operation_code == "<" or operation_code == "<=":
                try:
                    resultset02 = int(resultset)
                    resultset02 -= 1
                    resultset03 = str(resultset02)
                except ValueError:
                    resultset00 = resultset.split(".")
                    resultset000 = int(resultset00[0]) - 1
                    resultset03 = str(resultset000)
            elif operation_code == "in":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0])
            elif operation_code == "!in":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0] + "1")  # 待完善
            elif operation_code == "!=":
                resultset03 = str(resultset + "1")  # 待完善
            elif operation_code == "==":
                resultset03 = str(resultset)
            elif operation_code == "strEquals":
                resultset03 = str(resultset)
            elif operation_code == "!strEquals":
                if entry_code == "Name":
                    resultset0 = str(resultset)
                    resultset00 = resultset0[0:-1]
                    resultset03 = resultset00
                else:
                    resultset03 = str(resultset) + "1"
            elif operation_code == "None":
                resultset03 = None
            elif operation_code == "!None":
                resultset03 = resultset
            elif operation_code == "!include":
                resultset0 = resultset[0]
                resultset00 = resultset0 + "1"
                resultset000 = resultset[1:]
                resultset03 = resultset00 + resultset000
            elif operation_code == "include":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0])
            elif operation_code == "!mod":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 + resultset01 + 1
                resultset03 = str(resultset01_1)
            elif operation_code == "mod":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 * resultset01
                resultset03 = str(resultset01_1)
            elif operation_code == "startsWith":
                resultset03 = str(resultset)
            elif operation_code == "length_less":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            elif operation_code == "chinese_length_less":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            elif operation_code == "!length":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            elif operation_code == "notRegex":
                resultset03 = str(resultset + 'a')
            elif operation_code == "length_big":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 + 1
                resultset03 = str(resultset01_1)
            elif operation_code == "to_yyyy":
                resultset03 = str(resultset)
            elif operation_code == "floatPart":
                resultset03 = str(resultset)
            elif operation_code == "to_mm":
                resultset03 = str(resultset)
            elif operation_code == "floor":
                resultset03 = str(resultset)
            elif operation_code == "to_dd":
                resultset03 = str(resultset)
            elif operation_code == "regex":
                resultset03 = str(resultset)
            elif operation_code == "endsWith":
                resultset03 = str(resultset)
            elif operation_code == "length":
                resultset03 = str(resultset)
                # 给insuredList02字典的entry_code02字段赋resultset02值
            subPolList02[entry_code02] = resultset03
            bom01["subPolList"] = [subPolList02]

        # 保单
        elif object_code == "BomCont":
            resultset03 = 0
            if operation_code == ">" or operation_code == ">=":
                try:
                    resultset02 = int(resultset)
                    resultset02 += 1
                    resultset03 = str(resultset02)
                except ValueError:
                    resultset00 = resultset.split(".")
                    resultset000 = int(resultset00[0]) + 1
                    resultset03 = str(resultset000)
            elif operation_code == "<" or operation_code == "<=":
                try:
                    resultset02 = int(resultset)
                    resultset02 -= 1
                    resultset03 = str(resultset02)
                except ValueError:
                    resultset00 = resultset.split(".")
                    resultset000 = int(resultset00[0]) - 1
                    resultset03 = str(resultset000)
            elif operation_code == "in":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0])
            elif operation_code == "!in":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0] + "1")  # 待完善
            elif operation_code == "!=":
                resultset03 = str(resultset + "1")  # 待完善
            elif operation_code == "==":
                resultset03 = str(resultset)
            elif operation_code == "strEquals":
                resultset03 = str(resultset)
            elif operation_code == "!strEquals":
                if entry_code == "Name":
                    resultset0 = str(resultset)
                    resultset00 = resultset0[0:-1]
                    resultset03 = resultset00
                else:
                    resultset03 = str(resultset) + "1"
            elif operation_code == "None":
                resultset03 = None
            elif operation_code == "!None":
                resultset03 = resultset
            elif operation_code == "!include":
                resultset0 = resultset[0]
                resultset00 = resultset0 + "1"
                resultset000 = resultset[1:]
                resultset03 = resultset00 + resultset000
            elif operation_code == "include":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0])
            elif operation_code == "!mod":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 + resultset01 + 1
                resultset03 = str(resultset01_1)
            elif operation_code == "mod":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 * resultset01
                resultset03 = str(resultset01_1)
            elif operation_code == "startsWith":
                resultset03 = str(resultset)
            elif operation_code == "length_less":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            elif operation_code == "chinese_length_less":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            elif operation_code == "!length":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            # 给insuredList02字典的entry_code02字段赋resultset02值
            bomCont02[entry_code02] = resultset03
            bom01["bomCont"] = bomCont02
        # 销售
        elif object_code == "BomSale":
            resultset03 = 0
            if operation_code == ">" or operation_code == ">=":
                try:
                    resultset02 = int(resultset)
                    resultset02 += 1
                    resultset03 = str(resultset02)
                except ValueError:
                    resultset00 = resultset.split(".")
                    resultset000 = int(resultset00[0]) + 1
                    resultset03 = str(resultset000)
            elif operation_code == "<" or operation_code == "<=":
                try:
                    resultset02 = int(resultset)
                    resultset02 -= 1
                    resultset03 = str(resultset02)
                except ValueError:
                    resultset00 = resultset.split(".")
                    resultset000 = int(resultset00[0]) - 1
                    resultset03 = str(resultset000)
            elif operation_code == "in":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0])
            elif operation_code == "!in":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0] + "1")  # 待完善
            elif operation_code == "!=":
                resultset03 = str(resultset + "1")  # 待完善
            elif operation_code == "==":
                resultset03 = str(resultset)
            elif operation_code == "strEquals":
                resultset03 = str(resultset)
            elif operation_code == "!strEquals":
                if entry_code == "Name":
                    resultset0 = str(resultset)
                    resultset00 = resultset0[0:-1]
                    resultset03 = resultset00
                else:
                    resultset03 = str(resultset) + "1"
            elif operation_code == "None":
                resultset03 = None
            elif operation_code == "!None":
                resultset03 = resultset
            elif operation_code == "!include":
                resultset0 = resultset[0]
                resultset00 = resultset0 + "1"
                resultset000 = resultset[1:]
                resultset03 = resultset00 + resultset000
            elif operation_code == "include":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0])
            elif operation_code == "!mod":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 + resultset01 + 1
                resultset03 = str(resultset01_1)
            elif operation_code == "mod":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 * resultset01
                resultset03 = str(resultset01_1)
            elif operation_code == "startsWith":
                resultset03 = str(resultset)
            elif operation_code == "length_less":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            elif operation_code == "chinese_length_less":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            elif operation_code == "!length":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            # 给insuredList02字典的entry_code02字段赋resultset02值
            bomSale02[entry_code02] = resultset03
            bom01["bomSale"] = bomSale02

        elif object_code == "BomPolicy,BomAppnt":
            if operation_code == "/,>" or operation_code == "/,>=":
                entry_code03 = entry_code02.split(",")
                entry_code04 = entry_code03[0]  # 是BomPolicy里面的某个字段
                entry_code05 = entry_code03[1]
                # 将接口字段首字母转为小写
                a = entry_code05[0]
                b = entry_code05[1:]
                c = str.lower(a)
                entry_code06 = c + b  # 是BomAppnt里面的某个字段

                # 切分小数点
                resultset02 = resultset.split(".")
                resultset02 = int(resultset02[0])
                resultset02 += 2
                resultset03 = str(resultset02)

                bomPolicy02[entry_code04] = resultset03
                bomAppnt02[entry_code06] = "1"
                bom01["bomPolicy"] = bomPolicy02
                bom01["bomAppnt"] = bomAppnt02

        elif object_code == "BomInsured,BomInsured":
            if operation_code == "/,>":
                entry_code03 = entry_code02.split(",")
                entry_code04 = entry_code03[0]  # 是BomInsured里面的某个字段
                entry_code05 = entry_code03[1]
                # 将接口字段首字母转为小写
                a = entry_code05[0]
                b = entry_code05[1:]
                c = str.lower(a)
                entry_code06 = c + b  # 是BomInsured里面的某个字段

                resultset02 = int(resultset)
                resultset02 += 1
                resultset03 = str(resultset02)
                insuredList02[entry_code04] = resultset03
                insuredList02[entry_code06] = "1"
                bom01["insuredList"] = [insuredList02]
            elif operation_code == "+,!length":
                entry_code03 = entry_code02.split(",")
                entry_code04 = entry_code03[0]  # 是BomInsured里面的某个字段
                entry_code05 = entry_code03[1]
                # 将接口字段首字母转为小写
                a = entry_code05[0]
                b = entry_code05[1:]
                c = str.lower(a)
                entry_code06 = c + b  # 是BomInsured里面的某个字段

                insuredList02[entry_code04] = "13966880013"
                insuredList02[entry_code06] = "86"
                bom01["insuredList"] = [insuredList02]

        elif object_code == "BomAppnt,BomAppnt":
            if operation_code == "/,>":
                entry_code03 = entry_code02.split(",")
                entry_code04 = entry_code03[0]  # 是BomInsured里面的某个字段
                entry_code05 = entry_code03[1]
                # 将接口字段首字母转为小写
                a = entry_code05[0]
                b = entry_code05[1:]
                c = str.lower(a)
                entry_code06 = c + b  # 是BomInsured里面的某个字段

                resultset02 = int(resultset)
                resultset02 += 1
                resultset03 = str(resultset02)
                insuredList02[entry_code04] = resultset03
                insuredList02[entry_code06] = "1"
                bom01["insuredList"] = [insuredList02]
            elif operation_code == "+,!length":
                entry_code03 = entry_code02.split(",")
                entry_code04 = entry_code03[0]  # 是BomInsured里面的某个字段
                entry_code05 = entry_code03[1]
                # 将接口字段首字母转为小写
                a = entry_code05[0]
                b = entry_code05[1:]
                c = str.lower(a)
                entry_code06 = c + b  # 是BomInsured里面的某个字段

                bomAppnt02[entry_code04] = "13966880013"
                bomAppnt02[entry_code06] = "86"
                bom01["bomAppnt"] = [bomAppnt02]

        elif object_code == "BomPolicy,BomPolicy":
            if operation_code == "-,<=":
                entry_code03 = entry_code02.split(",")
                entry_code04 = entry_code03[0]  # 是BomPolicy里面的某个字段
                entry_code05 = entry_code03[1]
                # 将接口字段首字母转为小写
                entry_code06 = ""  # 是BomPolicy里面的某个字段
                c = 0
                for i in range(len(entry_code05)):
                    a = entry_code05[i]
                    if a.isupper() and c == 0:
                        b = str.lower(a)
                        entry_code06 += b
                    else:
                        c += 1
                        entry_code06 += a

                resultset03 = str(resultset)
                bomPolicy02[entry_code04] = resultset03
                bomPolicy02[entry_code06] = resultset03
                bom01["bomPolicy"] = bomPolicy02

        elif object_code == "BomAppnt,BomMainPol":
            if operation_code == "+,>":
                entry_code03 = entry_code02.split(",")
                entry_code04 = entry_code03[0]  # 是BomAppnt里面的某个字段
                entry_code05 = entry_code03[1]
                # 将接口字段首字母转为小写
                a = entry_code05[0]
                b = entry_code05[1:]
                c = str.lower(a)
                entry_code06 = c + b  # 是BomMainPol里面的某个字段

                resultset02 = int(resultset)
                resultset02 += 1
                resultset03 = str(resultset02)
                bomAppnt02[entry_code04] = resultset03
                mainPolList02[entry_code06] = "1"
                bom01["bomAppnt"] = bomAppnt02
                bom01["mainPolList"] = [mainPolList02]

        elif object_code == "BomInsured,BomMainPol":
            if operation_code == "+,>":
                entry_code03 = entry_code02.split(",")
                entry_code04 = entry_code03[0]  # 是BomAppnt里面的某个字段
                entry_code05 = entry_code03[1]
                # 将接口字段首字母转为小写
                a = entry_code05[0]
                b = entry_code05[1:]
                c = str.lower(a)
                entry_code06 = c + b  # 是BomMainPol里面的某个字段

                resultset02 = int(resultset)
                resultset02 += 1
                resultset03 = str(resultset02)
                insuredList02[entry_code04] = resultset03
                mainPolList02[entry_code06] = "1"
                bom01["insuredList"] = [insuredList02]
                bom01["mainPolList"] = [mainPolList02]

        elif object_code == "BomMainPol,BomPolicy":
            if operation_code == "/,>":
                entry_code03 = entry_code02.split(",")
                entry_code04 = entry_code03[0]  # 是BomInsured里面的某个字段
                entry_code05 = entry_code03[1]
                # 将接口字段首字母转为小写
                a = entry_code05[0]
                b = entry_code05[1:]
                c = str.lower(a)
                entry_code06 = c + b  # 是BomInsured里面的某个字段

                # 切分小数点
                resultset02 = resultset.split(".")
                if resultset02[0] == "0":
                    resultset02 = int(resultset02[1])
                    resultset03 = str(resultset02)
                else:
                    resultset02 = int(resultset02[0])
                    resultset02 += 1
                    resultset03 = str(resultset02)

                mainPolList02[entry_code04] = resultset03
                bomPolicy02[entry_code06] = "1"
                bom01["mainPolList"] = [mainPolList02]
                bom01["bomPolicy"] = [bomPolicy02]

        elif object_code == "BomInsured,BomPolicy":
            if operation_code == "-,>":
                entry_code03 = entry_code02.split(",")
                entry_code04 = entry_code03[0]  # 是BomAppnt里面的某个字段
                entry_code05 = entry_code03[1]
                # 将接口字段首字母转为小写
                a = entry_code05[0]
                b = entry_code05[1:]
                c = str.lower(a)
                entry_code06 = c + b  # 是BomMainPol里面的某个字段

                resultset02 = int(resultset)
                resultset02 += 2
                resultset03 = str(resultset02)
                insuredList02[entry_code04] = resultset03
                bomPolicy02[entry_code06] = "1"
                bom01["insuredList"] = [insuredList02]
                bom01["bomPolicy"] = bomPolicy02

        # 代理人
        elif object_code == "BomAgent":
            resultset03 = 0
            if operation_code == ">" or operation_code == ">=":
                try:
                    resultset02 = int(resultset)
                    resultset02 += 1
                    resultset03 = str(resultset02)
                except ValueError:
                    resultset00 = resultset.split(".")
                    resultset000 = int(resultset00[0]) + 1
                    resultset03 = str(resultset000)
            elif operation_code == "<" or operation_code == "<=":
                try:
                    resultset02 = int(resultset)
                    resultset02 -= 1
                    resultset03 = str(resultset02)
                except ValueError:
                    resultset00 = resultset.split(".")
                    resultset000 = int(resultset00[0]) - 1
                    resultset03 = str(resultset000)
            elif operation_code == "in":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0])
            elif operation_code == "!in":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0] + "1")  # 待完善
            elif operation_code == "!=":
                resultset03 = str(resultset + "1")  # 待完善
            elif operation_code == "==":
                resultset03 = str(resultset)
            elif operation_code == "strEquals":
                resultset03 = str(resultset)
            elif operation_code == "!strEquals":
                if entry_code == "Name":
                    resultset0 = str(resultset)
                    resultset00 = resultset0[0:-1]
                    resultset03 = resultset00
                else:
                    resultset03 = str(resultset) + "1"
            elif operation_code == "None":
                resultset03 = None
            elif operation_code == "!None":
                resultset03 = resultset
            elif operation_code == "!include":
                resultset0 = resultset[0]
                resultset00 = resultset0 + "1"
                resultset000 = resultset[1:]
                resultset03 = resultset00 + resultset000
            elif operation_code == "include":
                resultset02 = resultset.split(",")
                resultset03 = str(resultset02[0])
            elif operation_code == "!mod":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 + resultset01 + 1
                resultset03 = str(resultset01_1)
            elif operation_code == "mod":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 * resultset01
                resultset03 = str(resultset01_1)
            elif operation_code == "startsWith":
                resultset03 = str(resultset)
            elif operation_code == "length_less":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            elif operation_code == "chinese_length_less":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            elif operation_code == "!length":
                resultset01 = int(resultset)
                resultset01_1 = resultset01 - 1
                resultset03 = str(resultset01_1)
            # 给insuredList02字典的entry_code02字段赋resultset02值
            bomAgent02[entry_code02] = resultset03
            bom01["bomAgent"] = bomAgent02

        # 将险种编码添加到报文的mainPolList（每个报文都添加）
        if entry_code != "RiskCode":
            bom01["mainPolList"][0]["riskCode"] = rule_group
        """
        # 添加一级渠道
        if entry_code != "SaleChnl":
            bom01["saleChnl"] = sale_chnl3
        # 添加二级渠道
        if entry_code != "SellType":
            bom01["sellType"] = sell_type3
        """
        bom01["saleChnl"] = sale_chnl3  # 添加一级渠道
        bom01["sellType"] = sell_type3  # 添加二级渠道
        bom01["mainPolList"][0]["riskStyle"] = riskStyle3

    # 关闭数据库连接
    db.close()

    bom03 = json.dumps(bom01, sort_keys=True, indent=4, ensure_ascii=False)
    res.append(bom03)
    reslist.append(resu_ocode_ecode_ei)
    op = [res, reslist]
    return op


if __name__ == '__main__':
    # 利安外网
    # db = pymysql.connect(host="119.91.31.248", port=13306, user="root", password="chenchenchen", database="lian_dat_ww",
    #                      cursorclass=pymysql.cursors.DictCursor)
    # 中韩外网
    db = pymysql.connect(host="101.35.132.237", port=13306, user="root", password="1qaz@WSXcode", database="dc_rule",
                         cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = """
     SELECT DISTINCT
        l.cal_code,
        CASE l.channel 
        WHEN '00' THEN '00'
        WHEN '09' THEN '09'
        WHEN '05' THEN '05'
        WHEN '03' THEN '03'
        WHEN '13' THEN '13'
        WHEN '12' THEN '12'
        WHEN '02' THEN '02'
        END AS 'saleChnl',
        CASE 
        WHEN l.channel = '01' THEN '01'
        END AS 'sellType',
                    CASE l.product_type
                    WHEN '00' THEN '00'
                    WHEN '01' THEN '01'
                    WHEN '02' THEN '02'
                    WHEN '03' THEN '03'
										WHEN '04' THEN '04'
                    WHEN '05' THEN '05'
                    WHEN '06' THEN '06'
                    WHEN '07' THEN '07'
										WHEN '08' THEN '08'
                    WHEN '09' THEN '09'
                    WHEN '10' THEN '10'
                    END AS 'riskStyle',
        d.rule_result
    FROM
        lrruleinformation l,
        lrruledecisioninformat i,
        lrruledecisionresult d
    WHERE
        l.cal_code = i.cal_code
    AND i.decision_code = d.decision_code
    # AND l.state = '7'
    AND l.cal_code in ('P010100000011530')  
    #AND l.updated_time >= '2020-12-21'
    ORDER BY
        cal_code LIMIT 1000;
"""
    cursor.execute(sql)
    results = cursor.fetchall()
    cal_code2 = []
    sale_chnl2 = []  # 一级渠道
    sell_type2 = []  # 二级渠道
    riskStyle2 = []  # 险种种类
    rule_result2 = []  # 提示话术
    for row in results:
        print(row['cal_code'])
        cal_code = row['cal_code']
        sale_chnl = row['saleChnl']
        sell_type = row['sellType']
        riskStyle = row['riskStyle']
        rule_result = row['rule_result']
        cal_code2.append(cal_code)
        sale_chnl2.append(sale_chnl)
        sell_type2.append(sell_type)
        riskStyle2.append(riskStyle)
        rule_result2.append(rule_result)

    db.close()

    get01 = []
    get_cal_code = []
    case_name_index = []
    # 循环执行每一条规则
    j = 0
    for index, i in enumerate(cal_code2):
        print(i)
        get01 = get_mysql(i, sale_chnl2[j], sell_type2[j], riskStyle2[j])
        get_cal_code.append(i)
        case_name_index.append(index + 1)
        j += 1

    # 写入Excel
    writer = pd.ExcelWriter(r'D:\规则引擎\测试案例\111.xlsx')
    print("正在写入Excel...")
    # 写入第一张表
    for i in range(len(get01)):
        get02 = get01[i]
        df1 = pd.DataFrame({
            "case_name": case_name_index,
            "url": "http://127.0.0.1:9901/cont/validationContDetail",
            "params": get01[0],
            "cal_code": get_cal_code,
            "assertion": rule_result2,
            "resu_ocode_ecode_ei": get01[1],
            "PassOrNot": "规则被校验",
            "备注": ""
        })
        df1.to_excel(writer, sheet_name='Sheet1', index=False, header=True)
        # 设置列宽
        writer.sheets['Sheet1'].column_dimensions['A'].width = 10
        writer.sheets['Sheet1'].column_dimensions['C'].width = 70
        writer.sheets['Sheet1'].column_dimensions['D'].width = 17
        writer.sheets['Sheet1'].column_dimensions['E'].width = 50
        writer.sheets['Sheet1'].column_dimensions['F'].width = 40
        writer.sheets['Sheet1'].column_dimensions['G'].width = 20

    writer._save()
    print("写入Excel完成。")