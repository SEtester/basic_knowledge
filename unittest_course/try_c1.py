# print('111')
# 1 + '1'
# print('222')
# print('333')

print('111')
try:
    1 + '1'
except Exception as msg:
    # 通知钉钉
    print(f'msg：{msg}')

print('222')
print('333')
