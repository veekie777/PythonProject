# 预习
f = abs
def add(x, y, f):
    return f(x)**2 + f(y)**2

print(add(2, -3, f))

# map
print(tuple(map(abs, [-1, -5, -7])))
print(list(map(abs, [-1, -5, -7])))

# reduce
from functools import reduce
def add(x, y):
    return x - y

print(reduce(add, [9, 6, 1, 3]))

# 把list转为整数int
s = [1, 5, 4, 2, 3]
def fn(x, y):
    return x * 10 + y
def power(x, y):
    return x**2 + y**2

# print(reduce(fn, map(power, s)))     # ??????

# filter:过滤序列
def odd(n):
    return n % 2 == 1

print(list(filter(odd, [1, 2, 3, 4, 5, 6, 7])))
print(list(map(odd, [1, 2, 3, 4, 5, 6, 7])))

# sorted()函数就可以对list进行排序
print(sorted([-1, -9, 5, 6], key=abs))







# 开始正式学习
# 高阶函数


# 变量可以指向函数
x = abs           # 在这里，x代表的这个函数

print(x(-10))

# abs也可以变成其他的值。所以一般不要用这种特殊的内置关键字，作为变量名


# 传入函数
def add(x, y, f):
    return f(x) + f(y)

print(add(-2, 3, abs))      # abs是内置的函数方法，所以可以直接用


def pf(x):
    return x**2             # pf是我们自己定义的函数方法

print(add(2, 3, pf))






















