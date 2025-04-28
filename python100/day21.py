# 1  r只读(文本内容  r读  w截断之前写 a追加写  x写之前文件存在则报错)
# file = open('file.txt', 'r', encoding='utf-8')
# print(file.read())
# file.close()

# 2
# file = open('file.txt', 'r', encoding='utf-8')
# for line in file:
#     print(line, end='')
# file.close()

# file = open('file.txt', 'r', encoding='utf-8')
# lines = file.readlines()
# for line in lines:
#     print(line, end='')
# file.close()

# 3. a追加
# file = open('file.txt', 'a', encoding='utf-8')
# file.write('\n标题：《致橡树》')
# file.write('\n作者：舒婷')
# file.write('\n时间：1977年3月')
# file.close()

# 4. 异常处理   try..except..finally
# file = None
# try:
#     file = open('致橡树.txt', 'r', encoding='utf-8')
#     print(file.read())
# except FileNotFoundError:
#     print('无法打开指定的文件!')
# except LookupError:
#     print('指定了未知的编码!')
# except UnicodeDecodeError:
#     print('读取文件时解码错误!')
# finally:
#     if file:
#         file.close()

# 5 自定义异常
class InputError(ValueError):
    """自定义异常类型"""
    pass


def fac(num):
    """求阶乘"""
    if num < 0:
        raise InputError('只能计算非负整数的阶乘')
    if num in (0, 1):
        return 1
    return num * fac(num - 1)

# print(fac(-1))

# flag = True
# while flag:
#     num = int(input('n = '))
#     try:
#         print(f'{num}! = {fac(num)}')
#         flag = False
#     except InputError as err:
#         print(err)

# 6. try..with上下文管理器语法在文件操作完成后自动执行文件对象的close方法
# try:
#     with open('file.txt', 'r', encoding='utf-8') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('无法打开指定的文件!')
# except LookupError:
#     print('指定了未知的编码!')
# except UnicodeDecodeError:
#     print('读取文件时解码错误!')

# 7. 读写二进制文件（文本模式后面加个b）
# try:
#     with open('pic.jpg', 'rb') as file1:
#         data = file1.read()
#     with open('吉多.jpg', 'wb') as file2:
#         file2.write(data)
# except FileNotFoundError:
#     print('指定的文件无法打开.')
# except IOError:
#     print('读写文件时出现错误.')
# print('程序执行结束.')

# 8. 大文件处理方式
try:
    with open('pic.jpg', 'rb') as file1, open('吉多.jpg', 'wb') as file2:
        data = file1.read(512)
        while data:
            file2.write(data)
            data = file1.read(512)
except FileNotFoundError:
    print('指定的文件无法打开.')
except IOError:
    print('读写文件时出现错误.')
print('程序执行结束.')