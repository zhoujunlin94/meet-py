import time

# range(3600) [0, 3600)
total = 0
for i in range(1, 101):
    total += i
print(total)

total2 = 0
for i in range(2,101, 2):
    total2 += i
print(total2)
print(sum(range(2, 101, 2)))

total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(total)


total = 0
i = 2
while True:
    total += i
    i += 2
    if i > 100:
        break
print(total) 


total = 0
for i in range(1, 101):
    if i % 2 != 0:
        continue
    total += i
print(total)