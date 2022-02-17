# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 执行包：runscript

import function.common as func


ApiTest = func.ApiTest()
#自动写入文件名
FILENAME = ['login.ini','user.ini','rfp.ini']
for i in range(len(FILENAME)):
    """1.新建测试报告目录"""
    ApiTest.reset_report(filename=func.cs.CASE_PATH+FILENAME[i])

    """2.执行测试用例"""
    ApiTest.run_test(filename=func.cs.CASE_PATH+FILENAME[i])

    """3.统计测试报告结果"""
    ApiTest.write_report_result()
