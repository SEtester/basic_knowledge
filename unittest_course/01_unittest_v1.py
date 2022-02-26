import unittest


#  setp Arrange: 初始化测试对象或者准备测试数据   翻译字面：定义测试方法   翻译功能测试：准备我的测试步骤和测试数据
def add(num1, num2):  # num1 num2叫形参
    '''
    定义一个加法函数
    :param num1: 必须是数字
    :param num2: 必须是数字
    :return:
    '''
    return num1 + num2  # return的意思就是 add() 函数调用 返回一个值（内存地址）给你


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
    def test_01_add_success(self):
        # setp2 Act : 调用被测方法  翻译字面：调用测试方法  翻译功能测试：执行用例
        # add指的是一个内存地址，这个内存地址是一个定义好的空间，存放add里面的函数结构
        # add() 表示执行add内存地址指向的这个逻辑
        # 1，2是实际参数
        ret = add(1, 2)
        print(ret)
        expect = 3
        # setp3 Assert: 断言 翻译字面：assert方法比较数据   翻译功能测试：预期结果与实际结果的比较
        self.assertEqual(expect, ret)


if __name__ == '__main__':
    # __name__ 表当前的模块，名字 '__main__'
    unittest.main()
