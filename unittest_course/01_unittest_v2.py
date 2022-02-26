import unittest

from calculator_handler import add
from loguru import logger


# class 表示定义一个类，类是在程序启动的时候就会加载进内存
# unittest 测试类Test开头，不允许Test结尾
# 类需继承 unittest.TestCase
class TestDemo(unittest.TestCase):
    '''
    3A 法则
    http://class.itest.info/interface/3a
    Arrange: 初始化测试对象或者准备测试数据   翻译字面：定义测试方法   翻译功能测试：准备我的测试步骤和测试数据
    Act : 调用被测方法  翻译字面：调用测试方法  翻译功能测试：执行用例
    Assert: 断言   翻译字面：assert方法比较数据   翻译功能测试：预期结果与实际结果的比较
    '''

    # 测试用例有用例名字，在代码里面，测试方法就是测试用例名
    # 测试方法必须以test开头，test_case排序以ASCII排序, 可通过用例名来排序；方法二：用时插件，装饰器来处理
    def test_01_add_success_with_int(self):
        # setp2 Act : 调用被测方法  翻译字面：调用测试方法  翻译功能测试：执行用例
        # add指的是一个内存地址，这个内存地址是一个定义好的空间，存放add里面的函数结构
        # add() 表示执行add内存地址指向的这个逻辑
        # 1，2是实际参数
        ret = add(1, 2)
        logger.info(f'\n'
                    f'ret: {ret}')
        expect = 3
        # setp3 Assert: 断言 翻译字面：assert方法比较数据   翻译功能测试：预期结果与实际结果的比较
        self.assertEqual(expect, ret)

    def test_02_add_success_with_float_and_int(self):
        ret = add(1, 2.2)
        logger.info(f'\n'
                    f'ret: {ret}')
        expect = 3.2
        self.assertEqual(expect, ret)

    def test_03_add_success_with_float(self):
        '''
        计算机浮点型比较，要先四舍五入
        :return:
        '''
        ret = add(1.1, 2.2)
        logger.info(f'\n'
                    f'ret: {ret}')
        expect = 3.3

        self.assertEqual(expect, ret)

    # 自行补充其他加法成功的案例

    def test_04_add_error_with_null(self):
        '''
        是否必传也是属于冒烟
        :return:
        '''
        ret = add('', '')
        logger.info(f'\n'
                    f'ret: {ret}')
        expect = '缺少必传参数'

        self.assertEqual(expect, ret)

    def test_05_add_int_and_negative(self):
        ret = add(1, -2)
        logger.info(f'\n'
                    f'ret: {ret}')
        expect = -1

        self.assertEqual(expect, ret)

    '''
    1、 数字 + 纯数字字符串
    2、 数字 + 非纯数字符串
    '''
    def test_06_add_str_to_int(self):
        '''
        1、 数字 + 纯数字字符串
        :return:
        '''
        ret = add('1', -2)
        logger.info(f'\n'
                    f'ret: {ret}')
        expect = -1

        self.assertEqual(expect, ret)


    # def test_04_add_error_with_str(self):
    #     ret = add(1, '2')
    #     logger.info(f'\n'
    #                 f'ret: {ret}')
    #     expect = 3
    #
    #     self.assertEqual(expect, ret)

    #
    #     # def test_02_add_error(self):
    # #     ret = add(1, 2)
    #     expect = 3


if __name__ == '__main__':
    # __name__ 表当前的模块，名字 '__main__'
    unittest.main()
