# 返回函数:函数作为返回值

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1)              # 只返回了菜谱和食材，没有开始做
print(f1())            # 这时，才开始按照菜谱来做食材
print(f1 == f2)        # False，每次调用都会返回一个新的函数，即使传入相同的参数
print(f1() == f2())    # True，按照食谱加工后，结果都是相等的

# 闭包
# 返回的函数并没有立刻执行，而是直到调用了f()才执行
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
# f1 = count()[0]
# f2 = count()[1]
# f3 = count()[2]
print(f1)            # 这里只是返回了一个方法，还未运行，接着运行：
print(f2)            # 这里同理，只返回了方法
print(f3)
print(f1())          # 此时开始运行，但是因为用了同一个i，此时的i=3
print(f2())
print(f3())
# 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9

# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))     # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


# 使用闭包的变量
# 就是内层函数引用了外层函数的局部变量。如果只是读外层变量的值，我们会发现返回的闭包函数调用一切正常：
def inc():
    x = 0
    def fn():
        # 仅读取x的值:
        return x + 1
    return fn

f = inc()
print(f()) # 1
print(f()) # 1

# 但是，如果对外层变量赋值，由于Python解释器会把x当作函数fn()的局部变量，它会报错：
# 报错的原因是x作为局部变量并没有初始化，直接计算x+1是不行的
def inc():
    x = 0
    def fn():
        nonlocal x        # 所以需要在fn()函数内部加一个nonlocal x的声明。加上这个声明后，解释器把fn()的x看作外层函数的局部变量，它已经被初始化了，可以正确计算x+1。
        x = x + 1         # 内层函数，不能修改外层函数的值
        return x
    return fn

f = inc()
print(f()) # 1
print(f()) # 2










