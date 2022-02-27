import unittest

from loguru import logger

'''
pip install ddt
'''
from calculator_handler import add

'''
1、你的数据驱动怎么做？
- 你的数据放在哪里
    - python dict 字典， python 数组  （面试的时候不答，原因：数据分离，不用要语言里面的类型）
    - json 字符串
    - yaml 
- 你用什么工具进行用例的参数化

2、装饰器 （视频）
    - 函数定义域
    - 闭包
'''
'''
1、装饰器意义在于，不改变原来函数的内部结果，在函数调用前或后添加功能
'''

# 列表 里面的元素都是相同结构的字典
datas = [
    {"case": "1号用例", "num1": 1, "num2": 2, "expect": 2},
    {"case": "2号用例", "num1": 3, "num2": 4, "expect": 7},
]

datas2 = [
    [1, 2],
    [1.1, 2.2],
]
# 装饰器的本质就是闭包，装饰器是个语法糖，把上述3行代码（闭包调用）缩成一个"装饰器"，@闭包名，装饰在你想增加功能的函数上
# 装饰器（闭包）不改变原函数的调用方式
from ddt import ddt, data, unpack, file_data


@ddt
class TestDdtDemo(unittest.TestCase):  # 测试类继承unittest.TestCase

    @file_data('./file_data/json_data.json')  # 这句话的意思 相当于，把json文件读取出来，然后进行，反序列化
    def test_ddt_demo2(self, case, num1, num2):  # 函数没有self,函数放进类里面要加self,表示属于这个类的实例对象，改名叫方法
        logger.info(f'\n'
                    f'data:{case, num1, num2} ')

    # @data(*datas2)
    # @unpack
    # def test_ddt_demo2(self, num1, num2):  # 函数没有self,函数放进类里面要加self,表示属于这个类的实例对象，改名叫方法
    #     logger.info(f'\n'
    #                 f'num1:{num1} num2: {num2}')
    #     # num1, num2 = **datas
    #     # ret = add(**datas)
    #     # logger.info(f'\n'
    #     #             f'ret: {ret}')
    #
    #     # expect = 3.2
    #     # self.assertEqual(expect, ret)

    # @data(*datas)  # *列表
    # def test_ddt_demo(self, datas):
    #     # logger.info(f'\n'
    #     #             f'data: {datas}')
    #     # case = datas['case'] # 如果拿不到case会报错，找不到key
    #     case = datas.get('case')  # 如果拿不到case不会报错，默认等于None
    #     num1 = datas.get('num1')
    #     num2 = datas.get('num2')
    #     add_ret = add(num1, num2)
    #     logger.info(f'\n'
    #                 f'case:{case}\n'
    #                 f'add_ret: {add_ret}')
    #     # unittset的断言是封装好的 ，封装在 TestCase 里面，
    #     # 测试类继承后，直接使用，self.assert```
    #     # pytest用的是python原生自带 assert
    #     expect = datas.get('expect')
    #     logger.info(f'\n'
    #                 f'expect: {expect}\n'
    #                 f'add_ret: {add_ret}')
    #     try:
    #         self.assertEqual(expect, add_ret)
    #     except Exception as msg:
    #         # 通知钉钉，xx用例报错了
    #         logger.info(f'\n'
    #                     f'{case} 用例执行失败')
    #         raise AssertionError(msg)
    #     else:
    #         logger.info(f'\n'
    #                     f'{case} 用例执行成功')


if __name__ == '__main__':
    unittest.main()  # 运行文件中所有的测试用例

    # @data(*datas2)
    # @unpack
    # def test_ddt_demo2(self, num1, num2):
    #     logger.info(f'\n'
    #                 f'num1:{num1} num2: {num2}')
    #     # num1, num2 = **datas
    #     # ret = add(**datas)
    #     # logger.info(f'\n'
    #     #             f'ret: {ret}')
    #
    #     # expect = 3.2
    #     # self.assertEqual(expect, ret)

'''
知识回顾：
1、3A原则包含那几个步骤？
- 定一个被调方法，数据
- 

2、当前文件执行print(__name__)结果是什么？ 调用其他模块的 执行 print(__name__) 结果是什么？
- 当前文件打印 : __main__ = '__main__'，跨文件调用，其他文件的print(__name__) = '调用的模块名'
3、
'''

'''
什么是json
1、json是一个字符串，特定格式的字符串
2、网络传输只认识字符串
'''

'''
作业：
1、抄一遍课堂上讲解的例子，先盲从，抄过程中思考好记忆，半小时内还没解决不懂的问题，直接问
2、什么是json？json的格式是什么？什么是json的序列化与反序列化？
3、学习装饰器: https://www.bilibili.com/video/BV1QE41147hU?p=236
优先day17 day18
有时间再学 day19 多个装饰器叠加
4、预习和学习yaml文件，（字符串）
维基百科：https://zh.wikipedia.org/wiki/YAML
python yaml使用：https://blog.csdn.net/lmj19851117/article/details/78843486
python yaml使用: https://wsa.jianshu.io/p/d99abfaafdf6
'''
