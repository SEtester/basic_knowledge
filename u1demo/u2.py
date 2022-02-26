'''
unittest
'''

# 快速使用

import unittest  # 为什么能import 这个是个问题   这个问题涉及到以后开发

from loguru import logger

# 同级目录这么引用不会报错，如果出现，英文翻译：报错：超过顶层
from calculator_v2 import add  # 编辑器不知道你哪一些路径可以引用，sys.path, python会从sys.path里面寻找可引用包的路径
'''
path = ""
sys.path.insert(0,'路径'）
'''

# 学习  1、先定性， 2、 再定量  3、积累一定的量，量变引起质变

# 硬盘，内存 ,cpu  # 程序和代码又什么区别？  代码是在硬盘面的，程序是在内存？  涉及运行代码，都是在内存，打开文件，文件也在内存；保存文件的时候，是把内存里面的
# 内存存进硬盘
# 面试题：
# 1、日和查看服务端日志  tail -n 10 xxx.log  /  tail -n 10 -f xxx.log  持续侦测
# 2、服务端如何打开一个 10G 的日志  ， windows memory crash   ,  less 一页一页查看 / cat 服务端崩溃

# 测试类里面不要去写，你要测的方法 定义一个类或方法
# step1 :

'''
接口测试就是功能测试，黑盒测试，一个没有UI界面的测试，绕过前端web app
面试题： 接口测试和接口自动化测试一样吗？
接口一开始是手工的，在项目开发中，开发提交了接口，手工输入参数，或者用脚本/代码去测/postman
接口自动化，等项目代码冻结以后，把接口测试完成的脚本部署到服务端 自动执行
'''

# Test开头，不允许Test结尾
class TestDemo(unittest.TestCase):
    '''
    3A 原则
    Arrange: 初始化测试对象或者准备测试数据  # 翻译：定义一个类或方法    # 测试用例：定义一个测试用例，写这个测试用例的步骤和数据准备
    Act : 调用被测方法  # 翻译 调用方法，获得结果  # 测试工作： 执行用例
    Assert: 断言  # 翻译 比较数据 比较结果  # 测试用例执行： 预期结果与实际结果的比较
    '''

    # 测试方法以 test开头，不允许以test结尾
    # 方法名字，要简洁明了，方法名就是用例名
    # 用例的执行顺序，以ascll顺序执行
    '''
    cpu如何识别0和1
    低电位表示0 ，高电位表示1
    8个比特位，8个比特位表示一个字母或数字。
    0000 0001  7个低电位，一个高电位  
    https://segmentfault.com/a/1190000009633523
    '''
    '''
    用例顺序
    方法1：通过方法名字，ascll码排序
    方法2：通过插件，装饰器，强制设置顺序
    '''

    def test_01_add_success(self):
        # setp2: Act : 调用被测方法  # 翻译 调用方法，获得结果  # 测试工作： 执行用例
        ret = add(1, 2)
        logger.info('\n'
                    f'ret: {ret}')  # python3.5 / python3.6 以上的才可以使用
        # step3: Assert: 断言  # 翻译 比较数据 比较结果  # 测试用例执行： 预期结果与实际结果的比较
        expect = 3
        self.assertEqual(expect, ret)  # 即使框架里面没有封装好的assert方法，也没关系，可以直接import unittest; unittest.TestCase.assertEqual()

    def test_02_add_success_int_and_float_(self):
        ret = add(1, 2.3)
        logger.info('\n'
                    f'ret: {ret}')
        expect = 3.3
        self.assertEqual(expect, ret)

    def test_03_add_success_float(self):
        ret = add(1.1, 2.2)
        logger.info('\n'
                    f'ret: {ret}')
        expect = 3.3  # 约定返回结果，只保留1个小数
        self.assertEqual(expect, ret)

    def test_04_add_error_with_null(self):
        ret = add('', '')
        logger.info('\n'
                    f'ret: {ret}')
        expect = '缺少必填参数'  # 约定返回结果，只保留1个小数
        self.assertEqual(expect, ret)

    '''
    1、纯数字的字符串相加
    2、纯数字的字符串+数字
    3、非纯数字的字符串 + 数字
    '''
    def test_05_add_success(self):
        ret = add('1.1', 1.1)
        logger.info('\n'
                    f'ret: {ret}')
        expect = 2.2  # 约定返回结果，只保留1个小数
        self.assertEqual(expect, ret)

if __name__ == '__main__':
    '''
    __name__ == __main__  print(f'当前文件：{__nam__}' ==> __main__  如果__name__ 在其他文件，打印出来的还是__main__ ？ 当前文件调用其他文件打印__name__
    __name__=='其他文件名'
    '''
    unittest.main()  # 执行当前文件的所有以test开头的用例，程序入口大部分是 main方法
