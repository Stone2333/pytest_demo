#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 @Author   : 石头
 @Time     : 2021/4/18 16:03
 @File     : path_setting.py
 @Project  : rd3-test-automation
"""

import os


class PathConfig:
    """路径类"""
    # 项目路径
    root_path = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
    # 测试数据路径
    case_data_path = os.path.join(root_path, 'casesdata')
    # 测试用例路径
    case_path = os.path.join(root_path, 'testcases')
    # 配置路径
    config_path = os.path.join(root_path, 'config')

