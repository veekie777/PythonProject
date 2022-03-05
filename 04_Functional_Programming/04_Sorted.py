# 排序算法
L = sorted([36, 5, -12, 9, -21])
print(L)
# 这就是高阶函数，按照绝对值排序
l = sorted([36, 5, -12, 9, -21], key=abs)
print(l)

# 字符串排序: 先大写，后小写
l = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(l)
# 如果不按照大小写排序
l = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(l)

# 反向排序，不必改动key函数，可以传入第三个参数reverse=True
l = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(l)

# 练习：

def so(x):
    return x[0].lower()

L = sorted([('Bob', 75), ('Adam', 92), ('bart', 66), ('lisa', 88)], key=so)
print(L)

# 再按成绩从高到低排序：
def score(x):
    return x[1]

L = sorted([('Bob', 75), ('Adam', 92), ('bart', 66), ('lisa', 88)], key=score, reverse=True)
print(L)







