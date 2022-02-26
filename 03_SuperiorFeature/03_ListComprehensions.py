# 列表生成式
print(list(range(1, 11)))
print(list(range(2, 11)))

# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做?
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)
# 但是很繁琐，所以：
rg = range(1, 11)          # 先把range拿出来, 从rg里拿一个给x, 再x*x操作
L = [x * x for x in rg]
print(L)

# 先从range拿，再if判断，再x*x操作
L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)

# 还可以使用两层循环，可以生成全排列：
L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)


import os
file = os.listdir('.')
print(file)

# if ... else:两种写法
# if放在后面，是筛选
L = [x for x in range(1, 11) if x % 2 == 0]
print(L)
# if放在前面，必须加else，表示判断
L = [x if x % 2 == 0 else -x for x in range(1, 11)]
print(L)









