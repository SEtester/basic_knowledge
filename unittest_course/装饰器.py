# 函数可以当做参数传递
# 闭包
def func_start(func):
    '''
    此函数的作用是，在函数执行之前，打印一句话
    '''

    def inner():
        print('---函数开始执行---')
        return func

    return inner


def func_start2(func):  # func就是一个形参
    '''
    此函数的作用是，在函数执行之前，打印一句话
    '''

    def inner():
        print('---函数开始执行---')
        print('---正在登录---')
        return func()

    return inner


@func_start2
def add():
    # print('---函数开始执行---')
    # print('---用户已登录---')
    print(f'num1:{1} , num2:{2}')
    # print('---函数执行结束---')



# inner = func_start2(jianfa)  # 变量 inner2 = inner函数的内存地址
# add = inner()  # 运行inner函数  ，拿到add内存地址
add()  # 运行add函数

# 装饰器的本质就是闭包，装饰器是个语法糖，把上述3行代码（闭包调用）缩成一个"装饰器"，@闭包名，装饰在你想增加功能的函数上
# 装饰器（闭包）不改变原函数的调用方式


@func_start2
def jianfa():
    # print('---函数开始执行---')
    # print('---用户已登录---')
    print(f'num3:{3} , num4:{4}')


jianfa()














# @func_start
# def add():
#     # print('---函数开始执行---')
#     # print('---用户已登录---')
#     print(f'num1:{1} , num2:{2}')
#     # print('---函数执行结束---')
#
#
# # 封闭开放
# # add()
# # 1、当我执行func_start(add) add是个内存
# inner = func_start(add)  # inner函数的内存地址，那么我可以执行
# add = inner() # 当我执行完inner函数后，打印---函数开始执行---'，返回func ——》 add函数的内存地址
# add()
