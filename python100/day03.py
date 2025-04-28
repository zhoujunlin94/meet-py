# 二进制
print(0b100)
# 八进制
print(0o100)
# 十进制
print(100)
# 十六进制
print(0x100)

print('-------------------')

# 浮点数
# 数字写法
print(1.23456)
# 科学计数法
print(1.23456e2)

# 字符串
print('-------------------')
print('hello')
print("hello")

print('-------------------')
print(True)
print(False)

# 变量
a = 45
b = 12
# print函数可以输出多个值，多个值之间可以用,进行分隔，输出的内容默认以空格分开。
print(a, b, a+b, a-b, a*b, a/b, a//b, a % b, a**b)


print('-------------------')
print(type(a))
b=1.23
print(type(b))
c='hello'
print(type(c))
d=True
print(type(d))

print('-------------------')
a = 100
b = 123.45
c = '123'
d = '100'
e = '123.45'
f = 'hello, world'
g = True
print(float(a))         # int类型的100转成float，输出100.0
print(int(b))           # float类型的123.45转成int，输出123
print(int(c))           # str类型的'123'转成int，输出123
print(int(c, base=16))  # str类型的'123'按十六进制转成int，输出291
print(int(d, base=2))   # str类型的'100'按二进制转成int，输出4
print(float(e))         # str类型的'123.45'转成float，输出123.45
print(bool(f))          # str类型的'hello, world'转成bool，输出True 任何非空字符串都是True
print(bool(''))         # 空字符串转成bool，输出False
print(int(g))           # bool类型的True转成int，输出1
print(chr(a))           # int类型的100转成str，输出'd'
print(ord('d'))         # str类型的'd'转成int，输出100