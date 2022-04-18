#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 @Author   : 石头
 @Time     : 2022/4/1 11:52
 @File     : conftest.py
 @Project  : rd3-test-automation
"""


import pytest
from allure import dynamic
import allure
from jsonpath import jsonpath

from common import tools
from config.path_setting import PathConfig
from config.api_path import Api


def pytest_generate_tests(metafunc):
    """
    根据用例方法名获取用例数据 并参数化传入测试数据

    :param metafunc:
    :return:
    """
    # 获取用例方法名
    test_name = metafunc.definition.name
    try:
        # 读取测试用例yaml
        test_data = tools.read_yaml(
            rf'{PathConfig.case_data_path}/{test_name}.yml')
        # 根据名字获取类属性
        api_info = getattr(Api, jsonpath(test_data, "$..url")[0])
        cases_info = test_data["cases_info"][0]
        # 更新读取的yaml
        cases_info["url"] = api_info.get("path")
        cases_info["method"] = api_info.get("method")
        # 判断只要测试方法传了args, cases_info就参数化传入数据
        if "cases_data" and "cases_info" in metafunc.fixturenames:
            # 参数化传入用例数据
            metafunc.parametrize("cases_data", test_data["cases_data"])
            metafunc.parametrize("cases_info", test_data["cases_info"])
    except FileNotFoundError:
        print("文件路径不存在")


def pytest_runtest_teardown(item, nextitem):
    """操作后钩子"""
    pass


def pytest_runtest_makereport(item, call):
    """
    钩子函数 动态修改用例标题

    :param item:
    :return:
    """
    pass

    # outcome = yield  # yield表示用例执行完后的步骤
    # rep = outcome.get_result()  # 获取测试结果相关信息
    # print('从结果中获取测试报告：', rep)
    # print('从报告中获取 nodeid：', rep.nodeid)
    # print('从报告中获取调用步骤：', rep.when)
    # print('从报告中获取执行结果：', rep.outcome)
    # print('用例执行结果', rep.when)
    # if rep.when == "call":
    #     # rep.when有三个值，setup，call，teardown不同的测试阶段
    #     dynamic.title("测测")
    # 以下动态添加只影响allure报告
    # dynamic.title("CaseName")    # 动态添加用例名称
    # dynamic.description("desc") # 动态添加用例描述
    # 动态添加用例级别
    # priority = _info.get("priority")
    # if priority == "高":
    #     dynamic.severity("critical")
    # elif priority == "中":
    #     dynamic.severity("normal")
    # elif priority == "低":
    #     dynamic.severity("minor")
