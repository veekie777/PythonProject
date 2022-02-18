# 位置参数
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def power2(x, n):
    return x ** n

# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5))

def power2(x, n=2):
    return x ** n

print(power2(5))

# 指定某个默认值
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('zhangsan', 'nan')
enroll('zhangsan', 'nan', 7)
enroll('zhangsan', 'nan', 7, 'Shanghai')
enroll('zhangsan', 'nan', city='Shanghai')
enroll('zhangsan', city='Shanghai', gender='nan')  # 指定了名字，可以乱序


# 默认参数，应该是不可变对象
def add_end(L=[]):
    L.append('END')
    return L

print(add_end())
print(add_end())

# 固定一个参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    print(sum)
# 传入的是一个tuple
calc((1, 2))               # 只能传入一个参数，或者一个tuple或list

# 可变参数
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

def calc(*numbers):
    print('接收到的是tuple', numbers)
    sum = 0
    for n in numbers:
        sum = sum + n * n
    print(sum)
# 传入的是多个参数
calc(1, 2, 3, 4, 5)


# 关键字参数
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# 如果参数名字能找到，则不放入关键字参数的dict中
# 如果找不到，则放入关键字参数dict中
person('Adam', 45, gender='M', job='Engineer')
person(name='Adam', age=45, gender='M', job='Engineer')

extra = {'gender': 'M', 'Job': 'Engineer'}
person('Jack', 24, **extra)      # 也可以先定义好dict（这里extra是dict）

# 命名关键字参数（很严格）
def person(name, age, *, city, job):
    print(name, age, city, job)

# person('Jack', 24)                                    #少了不行
# person('Jack', 24, 'Beijing', 'Engineer')             # 没有参数名也不行
person('Jack', 24, city='Beijing', job='Engineer')
# person('Jack', 24, city='Beijing', job='Engineer', zipcode=123456)    # 多了参数名, 也不行

def person(name, age, city, job):
    print(name, age, city, job)

# person('Jack', 24, 'Beijing', 'Engineer')             # 没有参数名也不行
person('Jack', 24, city='Beijing', job='Engineer')

# 参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)                        # a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, c=3)                   # a = 1 b = 2 c = 3 args = () kw = {}
f1(1, 2, 3, 'a', 'b')           # a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
f1(1, 2, 3, 'a', 'b', x=99)     # a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
f2(1, 2, d=99, ext=None)        # a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
print('----------1')
f1(args, 'bbb', **kw)           # a = (1, 2, 3, 4) b = bbb c = 0 args =  kw = {'d': 99, 'x': '#'}
f1(*args, **kw)                 # a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

print('----------2')
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)                 # a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}

# 练习
# 两个数相乘
def mul(x, y):
    return x * y

# 可接收一个或多个数并计算乘积
def mul(*numbers):
    if not numbers:
        raise TypeError('没有传任何的值')
    sum  = 1
    for n in numbers:
        sum  = sum * n
    return sum

print(mul(5, 6, 7))



print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')






