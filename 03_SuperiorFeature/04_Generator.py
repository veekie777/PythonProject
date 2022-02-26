# 生成器：要创建一个generator，有很多种方法
# 方法一：第一种方法很简单，只要把一个列表生成式的[]改成()
L = [x * x for x in range(10)]
g = (x * x for x in range(10))
print(g)

# for 循环 生成器
for n in g:
    print(n)

# 著名的斐波拉契数列（Fibonacci）
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(6)

# yield类似return， 但是是接力棒，标记下这次走到了哪里
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)


od = odd()
print(next(od))
print(next(od))

# 相当于创建一个流程，先做第一个，可以先去做其他事情，之后再回来，接着做流程中的事情
def operation():
    print('发送邮件')
    yield 1
    print('打印账单')
    yield(3)
    print('寄送账单')
    yield(5)
# 代办列表
opr = operation()
print(next(opr))
# cal ()
print(next(opr))
# 拿账单给领导签字
# 联系()
print(next(opr))

# 直接这么写，相当于每次重新开始走。相当于三个实例，每次只走了一次
next(odd())
next(odd())
next(odd())









