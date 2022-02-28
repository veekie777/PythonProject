# 定义函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-16))


def divide(x, y):
    if y == 0:
        return
    return x / y

print(int(divide(8, 2)))
print(divide(8, 0))
print(float(divide(8, 2)))
print('%f' % (divide(8, 2)))    # %f是默认打印小数点后6位
print('%9f' % (divide(8, 2)))   # 包括前面的空格和小数点，打印9位
print('%.9f' % (divide(8, 2)))  # 小数点后面一共打印9位


# 参数检查
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('你传入的不是int or float')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(1))



# 函数可以返回多个值，放在Tuple里
def getResult(x):
    return x**2, x**3, x**4, x**5


print(getResult(2))

# 游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的坐标
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


# 函数里面，米有return，则会在最后返回none
def func():
    pass

print(func())



# 作业

# n = 1
# x = '*'
# while n <= 4:
#     print(x * n)
#     n = n + 1
#
# n = 1
# x = '*'
# while n <= 8:
#     print(x * n)
#     n = n + 1
#
# n = 1
# x = '*'
# while n <= 12:
#     print(x * n)
#     n = n + 1


def stair(t):
    n = 1
    x = '*'
    while n <= t:
        print(x * n)
        n = n + 1

stair(4)


# 预习：
# 计算x的n次方

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(3, 3))


def add_end(L=[]):
    L.append('END')
    return L

print(add_end([2, 3, 4]))

print(add_end())
print(add_end())
print(add_end())
print(add_end([7, 8]))


