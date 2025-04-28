import random

languages = ['Python', 'Java', 'C++']
languages.append('JavaScript')
print(languages)  # ['Python', 'Java', 'C++', 'JavaScript']
languages.insert(1, 'SQL')
print(languages)  # ['Python', 'SQL', 'Java', 'C++', 'JavaScript']

print('-------------------')

languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
if 'Java' in languages:
    languages.remove('Java')
if 'Swift' in languages:
    languages.remove('Swift')
print(languages)  # ['Python', 'SQL', C++', 'JavaScript']
languages.pop()
temp = languages.pop(1)
print(temp)       # SQL
languages.append(temp)
print(languages)  # ['Python', C++', 'SQL']
languages.clear()
print(languages)  # []

print('-------------------')

languages.append('Python')
languages.append('Python')
print(languages)  # ['Python', 'Python']
languages.remove('Python')
print(languages)  # ['Python'] 只删除一个

print('-------------------')

del languages[0]
print(languages)

print('-------------------')
items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
print(items.index('Python'))     # 0
# 从索引位置1开始查找'Python'
print(items.index('Python', 1))  # 5
print(items.count('Python'))     # 2
print(items.count('Kotlin'))     # 1
print(items.count('Swfit'))      # 0
# 从索引位置3开始查找'Java'
if 'Java' in items:
    print(items.index('Java', 2)) 
    #print(items.index('Java', 3))  # ValueError: 'Java' is not in list


print('-------------------')
items = ['Python', 'Java', 'C++', 'Kotlin', 'Swift']
items.sort()
print(items)  # ['C++', 'Java', 'Kotlin', 'Python', 'Swift']

items.sort(reverse=True)
print(items) 

items.reverse()
print(items)  # ['Swift', 'Python', 'Kotlin', 'Java', 'C++']


print('-------------------')

items = []
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        items.append(i)
print(items)

items = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print(items)


print('-------------------')
nums1 = [35, 12, 97, 64, 55]
nums2 = []
for num in nums1:
    nums2.append(num ** 2)
print(nums2)

nums2 = [num ** 2 for num in nums1]
print(nums2)

print('-------------------')

nums1 = [35, 12, 97, 64, 55]
nums2 = []
for num in nums1:
    if num > 50:
        nums2.append(num)
print(nums2)

nums2 = [num for num in nums1 if num > 50]
print(nums2)




print('-------------------')

scores = [[95, 83, 92], [80, 75, 82], [92, 97, 90], [80, 78, 69], [65, 66, 89]]
print(scores[0])
print(scores[0][1])


print('-------------------')
print([random.randrange(60, 101) for _ in range(3)])

scores = [[random.randrange(60, 101) for _ in range(3)] for _ in range(5)]

print(scores)

