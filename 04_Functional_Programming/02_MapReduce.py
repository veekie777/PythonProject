# Python内建了map()和reduce()函数

# map()函数接收两个参数，一个是函数，一个是Iterable
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

# map()作为高阶函数，事实上它把运算规则抽象了，
# 因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数

L = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(L)


# reduce:
# educe把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

from functools import reduce
def fn(x, y):
    return x * 10 + y

l = reduce(fn, [1, 3, 5, 7, 9])
print(l)

# 把reduce和map结合
def fn(x, y):
    return x * 10 + y

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

L = reduce(fn, map(char2num, '13579'))
print(L)













