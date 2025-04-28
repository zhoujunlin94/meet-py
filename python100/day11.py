greet = '''hello
world
'''
print(greet)

s1 = '\'hello, world!\''
s2 = '\\hello, world!\\'
print(s1)
print(s2)

s1 = '\it \is \time \to \read \now'
# 只显示原始字符串
s2 = r'\it \is \time \to \read \now'
print(s1)
print(s2)

print('-------------------')
s1 = 'hello' + ', ' + 'world'
print(s1)    # hello, world
s2 = '!' * 3
print(s2)    # !!!
s1 += s2
print(s1)    # hello, world!!!
s1 *= 2
print(s1)    # hello, world!!!hello, world!!!

print('-------------------')
s1 = 'a whole new world'
s2 = 'hello world'
print(s1 == s2)             # False
print(s1 < s2)              # True
print(s1 == 'hello world')  # False
print(s2 == 'hello world')  # True
print(s2 != 'Hello world')  # True
s3 = '高顿'
print(ord('高'))    # 39640        
print(ord('顿'))    # 39039        
s4 = '高吨'
print(ord('吨'))    # 21544        
print(s3 >= s4)             # True
print(s3 != s4)             # True

print('-------------------')
s1 = 'hello, world'
s2 = 'goodbye, world'
print('wo' in s1)      # True
print('wo' not in s2)  # False
print(s2 in s1)        # False

print(len(s1))


print('-------------------')
s = 'abc123456'
n = len(s)
print(s[0], s[-n])    # a a
print(s[n-1], s[-1])  # 6 6
print(s[2], s[-7])    # c c
print(s[5], s[-4])    # 3 3
print(s[2:5])         # c12
print(s[-7:-4])       # c12
print(s[2:])          # c123456
print(s[:2])          # ab
print(s[::2])         # ac246
print(s[::-1])        # 654321cba


print('-------------------')
s1 = 'hello, world!'
# 字符串首字母大写
print(s1.capitalize())  # Hello, world!
# 字符串每个单词首字母大写
print(s1.title())       # Hello, World!
# 字符串变大写
print(s1.upper())       # HELLO, WORLD!
s2 = 'GOODBYE'
# 字符串变小写
print(s2.lower())       # goodbye
# 检查s1和s2的值  字符串是不可变类型，使用字符串的方法对字符串进行操作会产生新的字符串，但是原来变量的值并没有发生变化。
print(s1)               # hello, world
print(s2)               # GOODBYE

print('-------------------')
s = 'hello, world!'
print(s.find('or'))      # 8
print(s.find('or', 9))   # -1
print(s.find('of'))      # -1
print(s.index('or'))     # 8
# print(s.index('or', 9))  # ValueError: substring not found

s = 'hello world!'
print(s.find('o'))       # 4
print(s.rfind('o'))      # 7
print(s.rindex('o'))     # 7
# print(s.rindex('o', 8))  # ValueError: substring not found

print('-------------------')
s1 = 'hello, world!'
print(s1.startswith('He'))   # False
print(s1.startswith('hel'))  # True
print(s1.endswith('!'))      # True
s2 = 'abc123456'
# 是否纯数字
print(s2.isdigit())  # False
# 是否纯字母
print(s2.isalpha())  # False
# 字母和数字组合
print(s2.isalnum())  # True

print('-------------------')
s = 'hello, world'
print(s.center(20, '*'))  # ****hello, world****
print(s.rjust(20))        #         hello, world
print(s.ljust(20, '~'))   # hello, world~~~~~~~~
# 左侧补零
print('33'.zfill(5))      # 00033
print('-33'.zfill(5))     # -0033

print('-------------------')
a = 321
b = 123
print('%d * %d = %d' % (a, b, a * b))
print('{0} * {1} = {2}'.format(a, b, a * b))
print(f'{a} * {b} = {a * b}')

print('-------------------')
s1 = '   jackfrued@126.com  '
print(s1.strip())      # jackfrued@126.com
s2 = '~你好，世界~'
print(s2.lstrip('~'))  # 你好，世界~
print(s2.rstrip('~'))  # ~你好，世界

print('-------------------')
s = 'hello, good world'
print(s.replace('o', '@'))     # hell@, g@@d w@rld
# 第三个参数指定替换的次数。
print(s.replace('o', '@', 1))  # hell@, good world

print('-------------------')
s = 'I love you'
# 默认使用空格进行拆分
words = s.split()
print(words)            # ['I', 'love', 'you']
print('~'.join(words))  # I~love~you

print('-------------------')
s = 'I#love#you#so#much'
words = s.split('#')
print(words)  # ['I', 'love', 'you', 'so', 'much']
# 只拆分2个
words = s.split('#', 2)
print(words)  # ['I', 'love', 'you#so#much']


print('-------------------')
a = '高顿'
b = a.encode('utf-8')
c = a.encode('gbk')
print(b)                  
print(c)                  
print(b.decode('utf-8')) 
print(c.decode('gbk'))   
