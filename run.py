# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 执行包：runscript

import function.common as func
import os
import constants as cs
from pathlib import Path

ApiTest = func.ApiTest()
"""
    获取测试执行文件名列表
    NOTE：如果需要执行特定文件内的文件，只需要修改path变量
"""
path = cs.CASE_PATH
FILENAME = ApiTest.get_file(path)


for i in range(len(FILENAME)):
    """1.新建测试报告目录"""
    ApiTest.reset_report(filename=FILENAME[i])

    """2.执行测试用例"""
    ApiTest.run_test(filename=FILENAME[i])

    """3.统计测试报告结果"""
    ApiTest.write_report_result()
