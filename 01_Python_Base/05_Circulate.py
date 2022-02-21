# 循环 for in
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# 数字累加计算
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

# range(n),可以生成一个整数序列，再通过list()函数可以转换为list
list(range(5))              # [0, 1, 2, 3, 4]
# 生成0-100的整数序列
print(range(101))           # range(0, 101)
# 求0-100的整数之和
sum = 0
for x in range(101):
    sum = sum + x
    print(sum)


# while循环
# 0到99之间的奇数之和
# 方法一：
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# 方法二：
sum = 0
n = 1
while n < 100:
    sum = sum + n
    n = n + 2
print(sum)


# list里放满1到1000
x = []
n = 1
while 1 <= n <= 1000:
    x.append(n)
    n = n + 1
print(x)


# break: 在循环中，break语句可以提前退出循环
n = 1
while n <= 100:
    if n > 10:      # 当n = 11时，条件满足，执行break语句
        break       # break语句会结束当前循环
    print(n)
    n = n + 1
print('END', n)

n = 1
while n <= 100: 
    print(n)
    n = n + 1
    if n > 10:
        break
print('END', n)

n = 1
while n <= 100:
    print(n)
    if n > 10:
        break
    n = n + 1
print('END', n)

n = 1
while n <= 100:
    n = n + 1
    if n > 10:
        break
    print(n)
print('END', n)




# continue: continue的作用是提前结束本轮循环，并直接开始下一轮循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:      # 如果n是偶数，执行continue语句
        continue        # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

# 写一个死循环,打印7的倍数，并且可以被2整除
n = 0
while n >= 0:
    n = n + 1
    if n % 7 == 0:
        if n % 2 == 0:
            print(n)

n = 0
while True:
    n = n + 1
    if (n % 7 == 0) and (n % 2 == 0):
        print(n)



