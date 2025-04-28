import random
import string

# 0-9纯数字  a-z A-Z大小写字母
ALL_CHARS = string.digits + string.ascii_letters

def generate_code(*, code_len=4):
    """
    生成指定长度的验证码
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码字符串
    random模块的sample和choices函数都可以实现随机抽样，sample实现无放回抽样，这意味着抽样取出的元素是不重复的；choices实现有放回抽样，这意味着可能会重复选中某些元素。这两个函数的第一个参数代表抽样的总体，而参数k代表样本容量，需要说明的是choices函数的参数k是一个命名关键字参数，在传参时必须指定参数名。
    """
    return ''.join(random.choices(ALL_CHARS, k=code_len))

"""
is_prime函数的参数num后面的: int用来标注参数的类型，虽然它对代码的执行结果不产生任何影响，但是很好的增强了代码的可读性。同理，参数列表后面的-> bool用来标注函数返回值的类型，它也不会对代码的执行结果产生影响，但是却让我们清楚的知道，调用函数会得到一个布尔值，要么是True，要么是False。
"""
def is_prime(num: int) -> bool:
    """
    判断一个正整数是不是质数
    :param num: 大于1的正整数
    :return: 如果num是质数返回True，否则返回False
    """
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True