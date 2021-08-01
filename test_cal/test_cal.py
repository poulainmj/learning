'''
1、补全计算器（加法 除法）的测试用例
2、使用参数化完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
注意： 使用等价类，边界值，因果图等设计测试用例
测试用例中添加断言，验证结果
灵活使用 setup(), teardown() , setup_class(), teardown_class()
'''

import logging
from decimal import Decimal

import allure
import pytest
import yaml


class Test_method:
    def add(self, a, b):
        return a + b
        pass

    def div(self, a, b):
        return a / b
def open_data():
    with open("./data/cal_data.yaml") as f:
        data = yaml.safe_load(f)
    return data

@allure.feature("运算测试模块")
class Test_cal:
    def setup_class(self):
        self.cal = Test_method()
        logging.info("计算开始")

    def teardown_class(self):
        logging.info("计算结束")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("加法测试")
    @pytest.mark.parametrize('a,b,c',open_data()["add_data"], ids=open_data()["add_ids"])
    def test_add(self, a, b, c):
        if isinstance(a, float) or isinstance(b, float):
            assert Decimal(str(c)) == self.cal.add(Decimal(str(a)), Decimal(str(b)))
        else:
            assert c == self.cal.add(a, b)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("加法计算异常测试")
    @pytest.mark.parametrize('a,b,c',open_data()["add_data_fail"], ids=open_data()["add_ids_fail"])
    def test_add_fail(self, a, b, c):
        try:
            assert c == self.cal.add(a, b)
        except Exception as e:
            print(e)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("除法测试")
    @pytest.mark.parametrize('a,b,c',open_data()["div_data"], ids=open_data()["div_ids"])
    def test_div(self, a, b, c):
        if isinstance(a,float) or isinstance(b,float):
            assert Decimal(str(c)) == self.cal.div(Decimal(str(a)),Decimal(str(b)))
        else:
            assert c == self.cal.div(a,b)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("除法异常测试")
    @pytest.mark.parametrize('a,b,c',open_data()["div_data_fail"], ids=open_data()["div_ids_fail"])
    def test_div_fail(self, a, b, c):
        try:
            assert c == self.cal.div(a, b)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    pytest.main()
