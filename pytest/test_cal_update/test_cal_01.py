'''
    1.改造 计算器 测试用例，使用 fixture 函数获取计算器的实例

    2.计算之前打印开始计算，计算之后打印结束计算

    3.添加用例日志，并将日志保存到日志文件目录下

    4.生成测试报告，展示测试用例的标题，用例步骤，与测试日志，截图附到课程贴下
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

@pytest.fixture(scope="module",autouse=True)
def get_object():
    cal=Test_method()
    logging.info("计算开始")
    yield cal
    logging.info("计算结束")

def open_data():
    with open("./data/cal_data.yaml") as f:
        data = yaml.safe_load(f)
    return data


@allure.feature("运算测试模块")
class Test_cal:
    def setup(self):
        logging.info("开始")
        print("开始")

    def teardown(self):
        logging.info("结束")
        print("结束")

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("int/minus加法测试")
    @allure.title("计算")
    @pytest.mark.parametrize('a,b,c',open_data()["add_data"], ids=open_data()["add_ids"])
    def test_add(self,get_object, a, b, c):
        assert c == get_object.add(a, b)
        logging.info(f"{a}与{b}相加的计算结果为{c}")

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("float的加法测试")
    @pytest.mark.parametrize('a,b,c',open_data()["add_data_float"], ids=open_data()["add_ids_float"])
    def test_add_float(self,get_object, a, b, c):
        logging.info(f"{a}与{b}相加的计算结果为{c}")
        assert Decimal(str(c)) == get_object.add(Decimal(str(a)), Decimal(str(b)))

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("含字符串的加法异常测试")
    @pytest.mark.parametrize('a,b,c',open_data()["add_data_fail"], ids=open_data()["add_ids_fail"])
    def test_add_fail(self,get_object, a, b, c):
        with pytest.raises(TypeError) as e:
            assert c == get_object.add(a,b)
        logging.info(f"错误类型为：{e}")

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("int/minus除法测试")
    @pytest.mark.parametrize('a,b,c',open_data()["div_data"], ids=open_data()["div_ids"])
    def test_div(self,get_object, a, b, c):
        assert c == get_object.div(a,b)
        logging.info(f"{a}与{b}相除的计算结果为{c}")

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("float除法测试")
    @pytest.mark.parametrize('a,b,c',open_data()["div_data"], ids=open_data()["div_ids"])
    def test_div_float(self,get_object, a, b, c):
        assert Decimal(str(c)) == get_object.div(Decimal(str(a)),Decimal(str(b)))
        logging.info(f"{a}与{b}相除的计算结果为{c}")

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("除数为0的除法异常测试")
    @pytest.mark.parametrize('a,b,c',open_data()["div_data_fail"], ids=open_data()["div_ids_fail"])
    def test_div_fail(self,get_object, a, b, c):
        with pytest.raises(TypeError) as e:
            assert c == get_object.div(a,b)
        logging.info(f"错误类型为：{e}")

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("含字符串的除法异常测试")
    @pytest.mark.parametrize('a,b,c',open_data()["div_data_fail_zero"], ids=open_data()["div_ids_fail_zero"])
    def test_div_fail_zero(self,get_object, a, b, c):
        with pytest.raises(ZeroDivisionError) as e:
            assert c == get_object.div(a,b)
        logging.info(f"错误类型为：{e}")
        allure.attach.file('picture.jpg', name="哆啦A梦", attachment_type=allure.attachment_type.JPG)

if __name__ == "__main__":
    pytest.main()
