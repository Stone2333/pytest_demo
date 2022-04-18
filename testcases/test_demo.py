#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 @Author   : 石头
 @Time     : 2022/4/18 15:56
 @File     : test_demo.py
 @Project  : pytest_demo
"""
import pytest
from common.tools import read_yaml
from config.path_setting import PathConfig

red_data = read_yaml(f"{PathConfig.case_data_path}/test_login4.yml")


class TestDemo:
    """测试"""

    data1 = ['123', '123456']
    @pytest.mark.parametrize("username", data1)
    def test_login1(self, username):
        """使用官方装饰器传递1个参数"""
        print(f"login1 账号:{username}")

    data2 = [
        ('lowen', '123'),
        ('lowen', '12345678'),
        ('lowen', '1234567890123456'),
        ('lowenlowen', '12345678901234561')
    ]
    @pytest.mark.parametrize("username, password", data2)
    def test_login2(self, username, password):
        """使用官方装饰器传递多个参数数据"""
        print(f"login2 账号:{username}, 密码:{password}")

    @pytest.mark.parametrize("cases_data", red_data["cases_data"])
    def test_login3(self, cases_data):
        """读取yaml参数化传参"""
        print(f"login3 cases_data:{cases_data}")

    def test_login4(self, cases_info, cases_data):
        """使用钩子函数传递数据"""
        print(f"login4 cases_info:{cases_info}, cases_data:{cases_data}")

