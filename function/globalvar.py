#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    @author:xiangdan
    @file:globalvar.py
    @time:2022/02/09
"""


def _init():
    global _global_dict
    _global_dict = {}


def set_value(name, value):
    _global_dict[name] = value


def get_value(name, defvalue=None):
    try:
        return _global_dict[name]
    except KeyError:
        return defvalue
