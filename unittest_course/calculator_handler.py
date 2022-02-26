#  setp Arrange: 初始化测试对象或者准备测试数据   翻译字面：定义测试方法   翻译功能测试：准备我的测试步骤和测试数据
def add(num1, num2):  # num1 num2叫形参
    '''
    定义一个加法函数
    :param num1: 必须是数字
    :param num2: 必须是数字
    :return:
    '''

    # all([a1,a2])判断数组里面所有元素是否都为真 全为真返回true, 一个为假返回false 相当于  a1 and a2]
    # if not ( a1 and a2):
    if not all([num1, num2]):
        return '缺少必传参数'

    if isinstance(num1, str):
        if num1.isdigit():
            num1 = float(num1)

    # 这个叫短路逻辑，and 前面为真 才会继续执行，为假后面的不执行
    if isinstance(num2, str) and num2.isdigit():
        num2 = float(num2)

    # if not (num1.isdigit() and num1.isdigit()):
    #     return '参数异常'

    try:
        ret = num1 + num2
    except Exception as msg:
        return msg

    if isinstance(ret, float):
        ret = round(ret, 1)

    return ret  # return的意思就是 add() 函数调用 返回一个值（内存地址）给你
    # return 下面的逻辑不执行
    print('123')
