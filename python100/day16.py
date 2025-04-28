import operator
import functools
import operator

def calc(*args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = 0
    for item in items:
        if type(item) in (int, float):
            result += item
    return result

print(calc(1, 2, 3, 4, 5))  # 15

def calc(init_value, op_func, *args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = init_value
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item)
    return result

def add(x, y):
    return x + y


def mul(x, y):
    return x * y

# 调用函数需要在函数名后面跟上圆括号，而把函数作为参数时只需要函数名即可。
print(calc(0, add, 1, 2, 3, 4, 5))  # 15
print(calc(1, mul, 1, 2, 3, 4, 5))  # 120 


print(calc(0, operator.add, 1, 2, 3, 4, 5))  # 15
print(calc(1, operator.mul, 1, 2, 3, 4, 5))  # 120 



def is_even(num):
    """判断num是不是偶数"""
    return num % 2 == 0


def square(num):
    """求平方"""
    return num ** 2

old_nums = [35, 12, 8, 99, 60, 52]
new_nums = list(map(square, filter(is_even, old_nums)))
print(new_nums)  # [144, 64, 3600, 2704]

old_nums = [35, 12, 8, 99, 60, 52]
new_nums = [num ** 2 for num in old_nums if num % 2 == 0]
print(new_nums)  # [144, 64, 3600, 2704]

old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
new_strings = sorted(old_strings)
print(new_strings)  # ['apple', 'in', 'pear', waxberry', 'zoo']

old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
new_strings = sorted(old_strings, key=len)
print(new_strings)  # ['in', 'zoo', 'pear', 'apple', 'waxberry']


# 定义 lambda 函数的关键字是lambda，后面跟函数的参数，如果有多个参数用逗号进行分隔；冒号后面的部分就是函数的执行体，通常是一个表达式，表达式的运算结果就是 lambda 函数的返回值，不需要写return 关键字。
old_nums = [35, 12, 8, 99, 60, 52]
new_nums = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, old_nums)))
print(new_nums)  # [144, 64, 3600, 2704]


# 用一行代码实现计算阶乘的函数  reduce函数是 Python 标准库functools模块中的函数，它可以实现对一组数据的归约操作，类似于我们之前定义的calc函数，第一个参数是代表运算的函数，第二个参数是运算的数据，第三个参数是运算的初始值。很显然，reduce函数也是高阶函数，它和filter函数、map函数一起构成了处理数据中非常关键的三个动作：过滤、映射和归约。
fac = lambda n: functools.reduce(operator.mul, range(2, n + 1), 1)

# 用一行代码实现判断素数的函数 如果传入的序列中所有的布尔值都是True，all函数返回True，否则all函数返回False。
is_prime = lambda x: all(map(lambda f: x % f, range(2, int(x ** 0.5) + 1)))

# 调用Lambda函数
print(fac(6))        # 720
print(is_prime(37))  # True


"""
偏函数是指固定函数的某些参数，生成一个新的函数，这样就无需在每次调用函数时都传递相同的参数。
在 Python 语言中，我们可以使用functools模块的partial函数来创建偏函数。
例如，int函数在默认情况下可以将字符串视为十进制整数进行类型转换，如果我们修修改它的base参数，就可以定义出三个新函数，
分别用于将二进制、八进制、十六进制字符串转换为整数，
类似于Java中的重载
"""
int2 = functools.partial(int, base=2)
int8 = functools.partial(int, base=8)
int16 = functools.partial(int, base=16)

print(int('1001'))    # 1001

print(int2('1001'))   # 9
print(int8('1001'))   # 513
print(int16('1001'))  # 4097

#  partial函数的第一个参数和返回值都是函数，它将传入的函数处理成一个新的函数返回。