# Python内置了字典：dict的支持，dict全称dictionary
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# 这种key-value存储方式，在放进去的时候，必须根据key算出value的存放位置，这样，取的时候才能根据key直接拿到value

# 改变key值
d['Adam'] = 67
print(d['Adam'])
d['Adam'] = 71
print(d['Adam'])

# 如果key不存在，dict就会报错
# d['Thomas']

# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print('Thomas' in d)                      # False
# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('Thomas'))                    # 返回none
print(d.get('Thomas', -1))                # 返回指定的默认值

# 删除一个key，用pop(key)方法，对应的value也会从dict中删除
# 同样，不能删除没有的key
print(d.pop('Bob'))

# dict内部存放的顺序，和key放入的顺序是没有关系的，他有自己的顺序

# 哈希算法Hash: 一种加密算法，保证在Dict里的key对应的对象是唯一的（加密过

# SET: set和dict类似，也是一组key的集合，但不存储value
s = set([1, 2, 3])
print(s)
s = set([1, 1, 2, 2, 3, 3])     # set的好处就是帮你去重复。因为不像dict，不会记下后面的value
print(s)

# add(key)
s.add(4)
s.add(1)                       # 如果加入重复的1，打印出来也不会重复
s.add('1')
print(s)
# remove(key)
s.remove(4)
print(s)

# set可以看成数学意义上的无序和无重复元素的集合, 因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)               # 交集
s1 | s2                      # 并集
print(s1 | s2)

# 再议不可变对象
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
s = set([1, 2, 3])
tuple1 = (1, 2, 3)
tuple2 = (1, [2, 3])

s.add(tuple1)               # set只能放不能变的东西，set是只有key的dict
print(s)

d[3] = tuple2
print(d)
d[1] = tuple1
print(d)
d[tuple1] = tuple1         # dict里，key不能变（所以能放tuple1），但是value可以变
print(d)



# 作业
# 题目1: 打印楼梯
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# n = 1
# x = '*'
# while n <= 8:
#     print(x)
#     x = '*' * (n + 1)
#     n = n + 1

n = 1
x = '*'
while n <= 8:
    print(x * n)
    n = n + 1


# 题目2: 打印n阶楼梯
# *
# **
# ***
# ****
# ...
# ...
# *************
# **************
n = 1
x = '*'
while n <= 14:
    print(x)
    x = '*' * (n + 1)
    n = n + 1

# 题目3: 打印金字塔        n   x  sp
#      *                1   1   5
#     ***               2   3   4
#    *****              3   5   3
#   *******             4   7   2
#  *********
# ***********
# n1 = 1
# n2 = 5
# x1 = '*'
# x2 = ' '
# while n1 <= 11 and n2 >= 0:
#     s = x2 * n2 + x1 * n1 + x2 * n2
#     print(s)
#     n1 = n1 + 2
#     n2 = n2 - 1

n = 1
x1 = '*'
x2 = ' '
while n <= 6:
    space = 6 - n
    s = space * x2 + x1 * (2*n - 1)
    print(s)
    n = n + 1


n = 1
x1 = '*'
x2 = ' '
max = 100
while n <= max:
    space = ' ' * (max - n)
    star = x1 * (2*n - 1)
    print(space + star)
    n = n + 1


# 题目4: 打印n阶金字塔
#      *
#     ***
#    *****
#   .......
#  .........
# ***********
n1 = 1
n2 = 5
x1 = '*'
x2 = ' '
while n1 <= 11 and n2 >= 0:
    s = x2 * n2 + x1 * n1 + x2 * n2
    print(s)
    n1 = n1 + 2
    n2 = n2 - 1
    if n2 < 0:
        break
while n1 >= 11 and n1 < 20:
    n1 = n1 + 2
    s = x1 * n1
    print(s)



# 预习：《函数》

def myabs(x):
    if x >= 0:
        return (x)
    else:
        return (-x)
print(myabs(-55))
print(0)

# 定义一个什么事也不做的空函数，可以用pass语句
def nop():
    pass
print(nop())
# 实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
# 后面想好了这里的代码要做什么，再来改pass。不写pass，就有语法错误
# if age >= 18:
#     pass

# 参数检查：可以用内置函数isinstance()实现

# 返回多个值
# import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数
import math
x = math.sqrt(4)
print(int(x))
print('%.5f' % x)

# 计算x的平方
def power(x):
    return x ** 2
print(power(3))
print(int(power(4.15)))        # 四舍五入

# 计算x的n次方
# def power(x, n):
#     s = 1
#     while n > 0:



# 二进制
0
1
10   # 2
11
100
101
110
111
1000
1001  # 9

# 十六进制
0
1
2
3
4
5
6
7
8
9
A
B
C
D
E
F   # 15



