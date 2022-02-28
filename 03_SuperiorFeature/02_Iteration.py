# 迭代
L = range(10)
for x in L:
    print(x)

# 默认情况下，dict迭代的是key。
# 如果要迭代value，可以用for value in d.values()，
# 如果要同时迭代key和value，可以用for k, v in d.items()默认情况下，dict迭代的是key。
# 如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()

d = {'a': 1, 'b': 2, 'c': 3}
print(d)
for key in d:
    print(key)

print(d.values())
for value in d.values():
    print(value)

print(d.items())
for key, value in d.items():
    print(key, value)


# 字符串也是可迭代对象
for ch in 'ABC':
    print(ch)

# 如何判断一个对象是可迭代对象呢？
# 方法是通过collections.abc模块的Iterable类型判断：
from collections.abc import Iterable
print(isinstance('abc', Iterable))        # str是否可迭代
print(isinstance([1,2,3], Iterable))      # list是否可迭代
print(isinstance(123, Iterable))          # 整数是否可迭代

# 迭代的时候，获取索引
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
# 索引就是位置，下面的y就是位置
for y, value in enumerate('he is a boy.'):
    print(y, value)

print('666666666666666666666666666666')

s = 'he is a boy.'
n = -1
z = 'y'
for x in s:
    if x != z:
        n = n + 1
    elif x == z:
        n = n + 1
        print(n)



s = 'he is a boy.'
n = -1
for x in s:
    if x != 'y':
        n = n + 1
        continue
    elif x == 'y':
        print('y在字符串的位置:', n+1)



# 同时打印y和o的位置






def same(s, k):
    n = -1
    for x in s:
        if x != k:
            n = n + 1
            continue
        elif x == k:
           return ('%s在\'%s\'字符串的位置是%s:' % (k, s, n+1))

# print(same('h'))
# print(same('y'))
# print(same('a'))


print(same('sgjak', 'j'))
print(same('www.baidu.com', 'b'))
print(same('我爱你积极', '爱'))


for n, x in enumerate(s):
    if x == 'y':
        print(n)


# 练习
# 请使用迭代查找一个list中最大值，并返回一个tuple：

def large(a):
    n = 0
    for x in a:
        k = a[n + 1]
        if k <= x:
            n = n + 1
        elif k > x:
            y = k
            n = n + 1
        continue
# print(large([1, 4, 2 ,9, 6, 7, 3, 5 ]))

def large2(a):
    if a == []:
        return

    max = a[0]
    for x in a:
        if x > max:
            max = x
        else:
            pass
    return (max,)
print(large2([1, 4, 2 ,9, 6, 7, 3, 5 ]))
print(large2([-1]))
print(large2([]))


# 请使用迭代查找一个list中最小值，并返回一个tuple：

def small(s):
    min = s[0]
    for x in s:
        if x < min:
            min = x
        else:
            pass
    return (min)


print(small([2, 4, 1, 7, 8, 4, 3, 6, 2, 8]))


# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
lastyear = 72
thisyear = 85
increase = ((thisyear - lastyear) / lastyear) * 100
print(increase)
print('小明今年的成绩提高了%.1f%%' % (increase))



# 请用索引取出下面list的指定元素：
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 取Apple
x = L[0]
print(x[0])
# Python
y = L[1]
print(y[1])
# 取Lisa
c = L[2]
print(c[2])


# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数
def BMI(x, y):
    s = x / (y ** 2)
    if s < 18.5:
        print('您的体重过轻')
    elif s < 25:
        print('您的体重正常')
    elif s < 28:
        print('您的体重过重')
    elif s < 32:
        print('您的体重肥胖')
    elif s >= 32:
        print('您的体重严重肥胖')
    return format(s, '.2f')               # 保留2位小数

print(BMI(80.5, 1.75))



# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0的两个解

import math


def quadratic(a, b, c):
    v = b**2 - 4*a*c
    if v < 0 or a ==0:
        return
    if v >= 0 and a != 0:
        z = math.sqrt(v)
        x = (-b +- z) / (2 * a)
        return x


print(quadratic(1, 2, 1))




# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积
# def mul(x, y):
#     return x * y

def mul(*numbers):
    sum = 1
    for x in numbers:
        sum = x * sum
    return sum

print(mul(2, 2, 3, 2))


# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格
def trim(s):
    while len(s) > 0:
        if s[0] == ' ':
            s = s[1:]
            continue
        if s[-1] == ' ':
            s = s[:-1]
            continue
        return s

print(trim('  22 11 22  '))


# 练习：排序，list里的数字从大到小排序
def sort1(s):
    s.sort()
    a = []
    n = len(s)
    for x in s:
        a.append(s[n - 1])
        n = n - 1
        continue
    return a


print(sort1([2, 5, 1, 4, 2, 3, 5, 8, 9, 7, 4, 1]))


def sort2(s):
    s.sort()
    a = []
    for x in s:
        a.insert(0, x)
        continue
    return a


print(sort2([2, 5, 1, 4, 2, 3, 5, 8, 9, 7, 4, 1]))


def sort3(s):
    s.sort()
    s.reverse()    # 反转
    return s


print(sort3([2, 5, 1, 4, 2, 3, 5, 8, 9, 7, 4, 1]))


def sort4(s):
    a = []
    number = len(s)
    while number > 0:
        max = s[0]
        for x in s:
            if x >= max:
                max = x
                continue
            else:
                pass
        a.append(max)
        s.remove(max)
        number = number - 1
    a.reverse()
    return a


print(sort4([2, 5, 1, 4, 2, 3, 5, 8, 9, 7, 4, 1]))





