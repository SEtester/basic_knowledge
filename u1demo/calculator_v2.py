from loguru import logger


def add(num1, num2):
    # 基础扎实选手
    # and 前面的条件为ture 后面的才会执行
    if isinstance(num1, str) or isinstance(num2, str):
        try:
            num1 = float(num1)
            num2 = float(num2)
        except Exception as msg:
            logger.info(f'msg: {msg}')


    ret = num1 + num2
    if isinstance(ret, float):
        ret = round(ret, 1)
    return ret
