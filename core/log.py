#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: 赫本z
# 基础包: 日志服务
# import logging
#
# def get_logger():
#     global logPath
#     try:
#         logPath
#     except NameError:
#         logPath = ""
#     FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
#     logging.basicConfig(level=logging.INFO, format=FORMAT)
#     return logging

# coding=utf-8
import os
import sys
import logbook
from logbook import Logger, StreamHandler, FileHandler, TimedRotatingFileHandler
from logbook.more import ColorizedStderrHandler
"""
    只有切换到test_case路径下执行log才会记录到文件中。
"""
'''
    日志等级：
    critical    严重错误，会导致程序退出
    error	    可控范围内的错误
    warning	    警告信息
    notice	    大多情况下希望看到的记录
    info	    大多情况不希望看到的记录
    debug	    调试程序时详细输出的记录
'''

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


# BasePath = os.path.dirname(os.path.abspath('.'))


def log_type(record, handler):
    log = "[{date}] [{level}] [{filename}] [{func_name}] [{lineno}] {msg}".format(
        date=record.time,  # 日志时间
        level=record.level_name,  # 日志等级
        filename=os.path.split(record.filename)[-1],  # 文件名
        func_name=record.func_name,  # 函数名
        lineno=record.lineno,  # 行号
        msg=record.message  # 日志内容
    )
    return log


# 日志存放路径
LOG_DIR = rootPath + '/log'
# LOG_DIR = os.path.join("Log")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
# 日志打印到屏幕
log_std = ColorizedStderrHandler(bubble=True)
log_std.formatter = log_type
# 日志打印到文件
log_file = TimedRotatingFileHandler(
    os.path.join(LOG_DIR, '%s.log' % 'log'), date_format='%Y-%m-%d', bubble=True, encoding='utf-8')
log_file.formatter = log_type

# 脚本日志
run_log = Logger("global_log")


def init_logger():
    logbook.set_datetime_format("local")
    run_log.handlers = []
    run_log.handlers.append(log_file)
    run_log.handlers.append(log_std)
    return ""



# 实例化，默认调用
logger = init_logger()

# if __name__ == "__main__":
#     run_log.info("测试日志模块")

