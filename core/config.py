#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: 赫本z
# 基础包：配置服务

import configparser
from core.log import run_log as logger
import json
import core.request as request
import function.common as func
import function.globalvar as gl

# config = configparser.ConfigParser()
config = configparser.RawConfigParser()
# logger = log.get_logger()


def get_config(filename):
    """
    获取文件配置
    :param filename: 配置文件名
    :return: None
    """
    global config
    try:
        config.read(filename)
        return True
    except Exception as e:
        logger.error("读取配置失败 %s" % e)


def get_data(title, key):
    """
    参数配置
    :param title: 配置文件的头信息
    :param key: 配置文件的key值
    :return: 配置文件的value
    """
    try:
        value = config.get(title, key)
        return value
    except Exception as e:
        logger.error("获取参数失败 %s" % e)


def get_title_list():
    """
    获取所有title
    :return: title list
    """
    try:
        title = config.sections()

        # return str(title).decode("string_escape")
        return str(title)
        # return '\n'.join(title)
    except Exception as e:
        logger.error("获取title信息失败 %s", e)


def set_token(filename):
    """
    写入token值

    """
    if 'login.ini' not in filename:
        sections = eval(get_title_list())

        # 从temp文件读取token
        fo = open("temp.py", "r+")
        token = fo.read()
        # 从ini文件中读取headers
        # header = sections[1]
        headers_json = config[sections[1]]['headers']

        # str convert dict
        headers_dict = eval(headers_json)
        for k, v in headers_dict.items():
            if k == 'x-token':
                headers_dict['x-token'] = token
        # dict convert str
        headers_str = json.dumps(headers_dict)
        # 设置headers值
        config.set(sections[1], 'headers', headers_str)
        # 写入ini文件
        with open(filename, 'w') as configfile:
            config.write(configfile)