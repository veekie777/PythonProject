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


s = 'he is a boy.'
n = -1
for x in s:
    if x != 'y':
        n = n + 1
        continue
    elif x == 'y':
        print('y在字符串的位置:', n+1)


# 他同时打印y和o的位置

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
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：

L = []



