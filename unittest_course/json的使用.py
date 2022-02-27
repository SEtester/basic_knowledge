
'''
（正）序列化 ： 任意代码（java,js,python）语言中"字典或数组" 转成json字符串
 反  序列化 ： json字符串 转成 任意语言中的"字典或数组"
 json.dumps() # d的排序在前，比l小，dumps表示序列化
 json.loads() # l的排序在后, 比d大，loads表示反序列化
'''

import json

f = open('./file_data/json_data.json','r',encoding='utf-8')
json_data_str = f.read()
# print(json_data_str)
# print(f'json_data_str type:{type(json_data_str)}')
# print(f'分割线-------')
data_list = json.loads(json_data_str)
print(data_list)
print(f'data_dict type:{type(data_list)}')