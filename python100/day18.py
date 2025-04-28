class Student:

    def study(self, course_name):
        print(f'学生正在学习{course_name}.')

    def play(self):
        print(f'学生正在玩游戏.')

stu1 = Student()
stu2 = Student()
# 对象在内存中的地址
# print(stu1)   
# print(stu2)  
# print(hex(id(stu1)), hex(id(stu2)))   

# 通过“类.方法”调用方法
# 第一个参数是接收消息的对象
# 第二个参数是学习的课程名称
# Student.study(stu1, 'Python程序设计')    # 学生正在学习Python程序设计.
# 通过“对象.方法”调用方法
# 点前面的对象就是接收消息的对象
# 只需要传入第二个参数课程名称
# stu1.study('Python程序设计')             # 学生正在学习Python程序设计.

# Student.play(stu2)                      # 学生正在玩游戏.
# stu2.play()                             # 学生正在玩游戏. 


class Student:
    """学生"""

    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def study(self, course_name):
        """学习"""
        print(f'{self.name}正在学习{course_name}.')

    def play(self):
        """玩耍"""
        print(f'{self.name}正在玩游戏.')
    
    def __str__(self):
        return f'({self.name}, {self.age})'

# 调用Student类的构造器创建对象并传入初始化参数
stu1 = Student('zjl', 44)
stu2 = Student('王大锤', 25)
stu1.study('Python程序设计')    
stu2.play()                   

print(stu1)  
print(stu2)  
