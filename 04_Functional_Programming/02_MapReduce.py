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
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# 记住！！！reduce返回的是结果，不是list！所以前面不用加list；而map需要！！

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



# 练习题（1）：
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

# 方法一：
a = ['adam', 'LISA', 'barT']
def let(x):
    n = 0
    b = []
    while n < len(a):
        for x in a:
            x = a[n]
            b.append(x[0].upper() + x[1:].lower())
            n = n + 1
        return b

L = list(let(a))
print(L)

# 方法二：
def let(x):
    return x[0].upper() + x[1:].lower()

L = list(map(let, a))
print(L)



# 练习题（2）
# Python提供的sum()函数可以接受一个list并求和，
# 请编写一个prod()函数，可以接受一个list并利用reduce()求积

from functools import reduce
def prod(x, y):
    return x * y

l = reduce(prod, [3, 5, 7, 9])
print(l)


# 练习题（3）
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
s = '123.456'
def str2float(x, y):
    return x * 10 + y

def str(s):
    s = s.replace('.', '')
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': 'none'}
    return digits[s]

print(list(map(str, s)))
# L = reduce(str2float, map(str, s))
# print(L)






