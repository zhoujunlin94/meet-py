from random import randrange


def make_judgement(a, b, c):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b

print(make_judgement(1, 2, 3))  # False
print(make_judgement(4, 5, 6))  # True

print(make_judgement(b=2, c=3, a=1))  # False
print(make_judgement(c=6, b=4, a=5))  # True



# /前面的参数是强制位置参数  调用函数时只能按照参数位置来接收参数值的参数
def make_judgement(a, b, c, /):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b

# print(make_judgement(b=2, c=3, a=1))  #TypeError: make_judgement() got some positional-only arguments passed as keyword arguments: 'a, b, c'
print(make_judgement(1, 2, 3))

# *后面的参数是命名关键字参数  命名关键字参数只能通过“参数名=参数值”的方式来传递和接收参数
def make_judgement(*, a, b, c):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b

# print(make_judgement(1, 2, 3)) # TypeError: make_judgement() takes 0 positional arguments but 3 were given
print(make_judgement(b=2, c=3, a=1))

# Python 中允许函数的参数拥有默认值

# 定义摇色子的函数
# 函数的自变量（参数）n表示色子的个数，默认值为2
def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randrange(1, 7)
    return total

print(roll_dice())
print(roll_dice(3))


# 带默认值的参数必须放在不带默认值的参数之后
def add(a=0, b=0, c=0):
    return a + b + c


# 调用add函数，没有传入参数，那么a、b、c都使用默认值0
print(add())         # 0
# 调用add函数，传入一个参数，该参数赋值给变量a, 变量b和c使用默认值0
print(add(1))        # 1
# 调用add函数，传入两个参数，分别赋值给变量a和b，变量c使用默认值0
print(add(1, 2))     # 3
# 调用add函数，传入三个参数，分别赋值给a、b、c三个变量
print(add(1, 2, 3))  # 6


# 用星号表达式来表示args可以接收0个或任意多个参数
# 调用函数时传入的n个参数会组装成一个n元组赋给args
# 如果一个参数都没有传入，那么args会是一个空元组
def add(*args):
    print(type(args))  # <class 'tuple'>
    total = 0
    # 对保存可变参数的元组进行循环遍历
    for val in args:
        # 对参数进行了类型检查（数值型的才能求和）
        if type(val) in (int, float):
            total += val
    return total

# 在调用add函数时可以传入0个或任意多个参数
print(add())         # 0
print(add(1))        # 1
print(add(1, 2, 3))  # 6
print(add(1, 2, 'hello', 3.45, 6))  # 12.45


# 参数列表中的**kwargs可以接收0个或任意多个关键字参数
# 调用函数时传入的关键字参数会组装成一个字典（参数名是字典中的键，参数值是字典中的值）
# 如果一个关键字参数都没有传入，那么kwargs会是一个空字典
def foo(*args, **kwargs):
    print(args)
    print(kwargs)


foo(3, 2.1, True, name='骆昊', age=43, gpa=4.95)



def foo():
    print('hello, world!')


def foo():
    print('goodbye, world!')
    
foo()  # 大家猜猜调用foo函数会输出什么