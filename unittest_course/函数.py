def add(num1, num2):
    print(f"num1：{num1}, num2:{num2}")


# num1 ,num2 叫形式参数  形参
# add(1, 2)

# 用数组/元组的形式传参
add(*[1, 2])  # *数组，数组解包 unpack *[1,2] 解析成 1 和 2 两个参数
add(*(3, 4))  # *元组，元组解包

# 用字典的形式传参 # **字典 ，字典解包
add(**{"num1": 5, "num2": 6})


