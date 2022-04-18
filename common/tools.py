#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 @Author   : 石头
 @Time     : 2022/4/18 15:59
 @File     : tools.py
 @Project  : pytest_demo
"""

import os

import yaml


def read_yaml(yaml_path):
    """
    读取yaml文件

    :param yaml_path: yaml文件路径
    :return:
    """
    if not os.path.isfile(yaml_path):
        raise FileNotFoundError('文件路径不存在')
    f = open(yaml_path, 'r', encoding='utf-8')
    cfg = f.read()
    yaml_dict = yaml.load(cfg, Loader=yaml.FullLoader)
    return yaml_dict