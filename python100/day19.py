class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def study(self, course_name):
        print(f'{self.__name}正在学习{course_name}.')


stu = Student('王大锤', 20)
# stu.study('Python程序设计')
# __name是私有属性，外部不能直接访问   _name是受保护的属性，外部也不能直接访问 但是类里面的study方法中可以通过self.__name访问该属性。
# print(stu.__name)  # AttributeError: 'Student' object has no attribute '__name'
# 这样写可以访问私有属性
# print(stu._Student__name)  # 王大锤



class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('王大锤', 20)
stu.sex = '男'  # 给学生对象动态添加sex属性


class Student:
    # 如果不希望在使用对象时动态的为对象添加属性，可以使用 Python 语言中的__slots__魔法。
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('王大锤', 20)
# AttributeError: 'Student' object has no attribute 'sex'
# stu.sex = '男'


class Triangle(object):
    """三角形"""

    def __init__(self, a, b, c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c

    """
    可以直接使用类名.方法名的方式来调用静态方法和类方法，二者的区别在于，类方法的第一个参数是类对象本身，而静态方法则没有这个参数。简单的总结一下，对象方法、类方法、静态方法都可以通过“类名.方法名”的方式来调用，区别在于方法的第一个参数到底是普通对象还是类对象，还是没有接受消息的对象。
    """
    @staticmethod
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a + b > c and b + c > a and a + c > b

    # @classmethod
    # def is_valid(cls, a, b, c):
    #     """判断三条边长能否构成三角形(类方法)"""
    #     return a + b > c and b + c > a and a + c > b

    # 将方法变成属性
    @property
    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    @property
    def area(self):
        """计算面积"""
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
    
t = Triangle(3, 4, 5)
# print(f'周长: {t.perimeter}')
# print(f'面积: {t.area}')



class Person:
    """人"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f'{self.name}正在吃饭.')
    
    def sleep(self):
        print(f'{self.name}正在睡觉.')


class Student(Person):
    """学生"""
    
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title
    
    def teach(self, course_name):
        print(f'{self.name}{self.title}正在讲授{course_name}.')



stu1 = Student('白元芳', 21)
stu2 = Student('狄仁杰', 22)
tea1 = Teacher('武则天', 35, '副教授')
stu1.eat()
stu2.sleep()
tea1.eat()
stu1.study('Python程序设计')
tea1.teach('Python程序设计')
stu2.study('数据科学导论')
