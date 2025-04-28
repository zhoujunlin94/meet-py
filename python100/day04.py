a = 10
b = 3
a += b        # 相当于：a = a + b
a *= a + 2    # 相当于：a = a * (a + 2)
print(a) 




h = float(input("请输入华氏温度："))
s = (h - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (h, s))
print(f'{h:.1f}华氏度 = {s:.1f}摄氏度')