# 条件判断,if条件后面需要有冒号
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else

# if判断条件还可以简写
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x = 1
if x:
    print('True')

number = 0
str = ''
list = []
tuple = ()
# 这些都是False, 其他是True

# input
s = input('birth: ')
birth = int(s)                  # 返回的是字符串，所以要把字符串变成整数int
if birth < 2000:
    print('00前')
else:
    print('00后')








