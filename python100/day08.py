import random

items1 = [35, 12, 99, 68, 55, 35, 87]
items2 = ['Python', 'Java', 'Go', 'Kotlin']
items3 = [100, 12.3, 'Python', True]
print(items1)
print(type(items1))  
print(items2)  
print(items3)  


items4 = list(range(1, 10))
items5 = list('hello')
print(items4)  
print(items5)  


items5 = [35, 12, 99, 45, 66]
items6 = [45, 58, 29]
items7 = ['Python', 'Java', 'JavaScript']
print(items5 + items6)  
print(items6 + items7)  
items5 += items6
print(items5) 

# 重复次数
print(items6 * 3)  
print(items7 * 2) 


print(29 in items6)  # True
print(99 in items6)  # False
print('C++' not in items7)     # True
print('Python' not in items7)  # False


print('-------------------')

items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
print(items8[0])   # apple
print(items8[2])   # pitaya
print(items8[4])   # watermelon
items8[2] = 'durian'
print(items8)      # ['apple', 'waxberry', 'durian', 'peach', 'watermelon']
print(items8[-5])  # 'apple'
print(items8[-4])  # 'waxberry'
print(items8[-1])  # watermelon
items8[-4] = 'strawberry'
print(items8)      # ['apple', 'strawberry', 'durian', 'peach', 'watermelon']

print('-------------------')

print(items8[1:3:1])     # ['strawberry', 'durian']
print(items8[0:3:1])     # ['apple', 'strawberry', 'durian']
print(items8[0:5:2])     # ['apple', 'durian', 'watermelon']
print(items8[-4:-2:1])   # ['strawberry', 'durian']
print(items8[-2:-6:-1])  # ['peach', 'durian', 'strawberry', 'apple']



print('-------------------')
# 如果start值等于0，那么在使用切片运算符时可以将其省略；如果end值等于N，N代表列表元素的个数，那么在使用切片运算符时可以将其省略；如果stride值等于1，那么在使用切片运算符时也可以将其省略。
print(items8[1:3])     # ['strawberry', 'durian']
print(items8[:3:1])    # ['apple', 'strawberry', 'durian']
print(items8[::2])     # ['apple', 'durian', 'watermelon']
print(items8[-4:-2])   # ['strawberry', 'durian']
print(items8[-2::-1])  # ['peach', 'durian', 'strawberry', 'apple']


print('-------------------')
items8[1:3] = ['x', 'o']
print(items8)  # ['apple', 'x', 'o', 'peach', 'watermelon']


print('-------------------')
nums1 = [1, 2, 3, 4]
nums2 = list(range(1, 5))
nums3 = [3, 2, 1]
print(nums1 == nums2)  # True
print(nums1 != nums2)  # False
print(nums1 <= nums3)  # True
print(nums2 >= nums3)  # False

print('-------------------')
languages = ['Python', 'Java', 'C++', 'Kotlin']
for index in range(len(languages)):
    print(languages[index])

print('-------------------')
languages = ['Python', 'Java', 'C++', 'Kotlin']
for language in languages:
    print(language)


print('-------------------')
counters = [0] * 6
# 模拟掷色子记录每种点数出现的次数
for _ in range(6000):
    face = random.randrange(1, 7)
    counters[face - 1] += 1
    
# 输出每种点数出现的次数
for face in range(1, 7):
    print(f'{face}点出现了{counters[face - 1]}次')