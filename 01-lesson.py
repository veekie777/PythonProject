# print，在控制台会打印输出里面的内容
print("this is my python project!")

# x=2, 是定义x的内容是2
x = 2
# if，是对后面的内容进行判断，判断是真，打印print里的内容；否则执行else里面的内容
if x == 1:
    # indented four spaces
    print("x is 1.")
else:
    print("x is not 1!")

print("Hello, World!")

# python可以打印两种数字，整数和小数。
x = 7
print(x)
# 打印小数，可用x=7或者下面的方法，打印的就是小数
x = float(7)
print(x)
# 可以用不用的function（方法，比如int、float）来定义后面的内容
x = int(8.9)
print(x)

# 定义字符串，双引号或者单引号
str = "this is string"
print(str)
# \后面的字符，只是单纯的显示，没有语法的含义（只是为了让程序知道，不要弄混两个双引号）
str = "他说:\"你好\"！"
str = "他说:'你好'！"
str = '他说:"你好"！'

# 字符串拼接
hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

FirstName = "栋"
LastName = "徐"
FullName = LastName + " " + FirstName
print(FullName)

# 变量批量赋值
a, b = 4, 5
print(a, b)

lastname, firstname, gender = "徐", "栋", "男"
print(lastname, firstname, gender)
fullname = lastname + firstname
print(fullname, gender)

# 字符串和数字相加，不行！
a, b = 7, "3"
print(a, b)

mystring = "hello"
myfloat = float(10)
myint = 20
print(mystring, myfloat, myint)

