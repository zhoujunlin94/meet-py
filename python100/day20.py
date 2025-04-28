from enum import Enum
import random
from abc import ABCMeta, abstractmethod

class Suite(Enum):
    """花色(枚举)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)

# for suite in Suite:
#     print(f'{suite}: {suite.value}')

class Card:
    """牌"""

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    # 重写__repr__方法，返回牌的花色和点数
    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'  # 返回牌的花色和点数
    
    # 用于排序
    def __lt__(self, other):
        if self.suite == other.suite:
            return self.face < other.face   # 花色相同比较点数的大小
        return self.suite.value < other.suite.value   # 花色不同比较花色对应的值

class Poker:
    """扑克"""

    def __init__(self):
        self.cards = [Card(suite, face) 
                      for suite in Suite
                      for face in range(1, 14)]  # 52张牌构成的列表
        self.current = 0  # 记录发牌位置的属性

    def shuffle(self):
        """洗牌"""
        self.current = 0
        random.shuffle(self.cards)  # 通过random模块的shuffle函数实现随机乱序

    def deal(self):
        """发牌"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌可以发"""
        return self.current < len(self.cards)
    

class Player:
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []  # 玩家手上的牌

    def get_one(self, card):
        """摸牌"""
        self.cards.append(card)

    def arrange(self):
        """整理手上的牌"""
        self.cards.sort()


poker = Poker()
poker.shuffle()
players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
# 将牌轮流发到每个玩家手上每人13张牌
# for _ in range(13):
#     for player in players:
#         player.get_one(poker.deal())
# 玩家整理手上的牌输出名字和手牌
# for player in players:
#     player.arrange()
#     print(f'{player.name}: ', end='')
#     print(player.cards)



class Employee(metaclass=ABCMeta):
    """员工"""

    def __init__(self, name):
        self.name = name
    # 使用abstractmethod装饰器将其声明为抽象方法，所谓抽象方法就是只有声明没有实现的方法，声明这个方法是为了让子类去重写这个方法。
    @abstractmethod
    def get_salary(self):
        """结算月薪"""
        pass


class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self.working_hour = working_hour

    def get_salary(self):
        return 200 * self.working_hour


class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales=0):
        super().__init__(name)
        self.sales = sales

    def get_salary(self):
        return 1800 + self.sales * 0.05

emps = [Manager('刘备'), Programmer('诸葛亮'), Manager('曹操'), Programmer('荀彧'), Salesman('张辽')]
for emp in emps:
    # isinstance函数更加强大，因为它可以判断出一个对象是不是某个继承结构下的子类型，你可以简单的理解为type函数是对对象类型的精准匹配，而isinstance函数是对对象类型的模糊匹配。
    if isinstance(emp, Programmer):
        emp.working_hour = int(input(f'请输入{emp.name}本月工作时间: '))
    elif isinstance(emp, Salesman):
        emp.sales = float(input(f'请输入{emp.name}本月销售额: '))
    print(f'{emp.name}本月工资为: ￥{emp.get_salary():.2f}元')