# 匿名函数
# 当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便

l = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(l)
# [1, 4, 9, 16, 25, 36, 49, 64, 81]
# 对比：
def f(x):
    return x * x

# 这样子，要简单一点
f1 = lambda x: x * x
l3 = list(map(f1, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 同样，也可以把匿名函数作为返回值返回，比如：
def build(x, y):
    return lambda: x * x + y * y

g = build(2, 3)
print(g)          # 不会马上执行，这里只是返回方法
print(g())        # 现在才执行得出结果




# 练习
# 请用匿名函数改造下面的代码：
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)
L = list(filter(lambda n: n % 2, range(1, 20)))
print(L)







