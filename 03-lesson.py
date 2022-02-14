# 运算符：加减乘除
add = 1 + 2
sub = 7 - 4
mul = 4 * 3
div = 9 / 3
print(add, sub, mul, div)
print(int(div))
# 求余数
div = 10 % 3
print(div)


# 除法计算中，如何取余数,用%来取余数！
modulo = 17 % 3
print(modulo)
squared = 3 ** 2
cubed = 3 ** 3
print(squared, cubed)

helloworld = "hello" + " " +"world"
print(helloworld)

# 字符串，也可以重复很多次
lotsofyou = "you" * 3
print(lotsofyou)

# list也可以合并
even_numbers = [0, 2, 4, 6]
odd_numbers = [1, 3, 5]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

# list也可以重复！
number = [2, 4, 6]
print(number * 2)

# exercise
# x_list = [11, 23, 45, 44, 77, 29, 60, 65, 71, 22]
# y_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# big_list = [x_list * 10, y_list * 10]
# big_list = x_list + y_list
# print(big_list)



# string formatting: 字符串格式化. 这里的格式化不是指清空，是指按照模板格式来进行处理！
name = "Tom"
age = 88
print("hello, %s!" % name)
print("wow, %d!" % age)
print("hello" + "," + " " + name + "!")

name = "Alex"
age = 77
print("%s is very old, %s is %d" % (name, name, age))

# 不是字符串，也可以当成字符串来打印
number = [1, 2, 3]
print("this is %s" % number)

# 需要记住的参数说明符
# %s = string, %d =integers, %f = floating point numbers, %.<number of digits>f 小数点保留几位
salary = 2356.55555
print("my salary is %f" % salary)
print("my salary is %.2f" % salary)

# exercise
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your balance is %.2f"
print(format_string % data)

# 字符串的操作
astring = "hello world!"
# 打印字符串长度
print(len(astring))
# 找到o第一次出现的位置
print(astring.index("o"))
# 倒着数o最后一次出现的位置
print(astring.rindex("o"))
# 找到某个字符串一共出现了几次
print(astring.count("o"))


list = [1, 2, 2, 5, 4, 9, 7, 8, 7]
print(len(list))
print(list.count(7))
print(list.index(2))

# 打印从第3到7位置的字符串
astring = "Hello world!"
print(astring[3:7])
# 只有一个数字，就把那个位置的数字拿出来
print(astring[4])
# 只留冒号左边的数字，从第4个位置开始，到最后
print(astring[3:])
# 只留冒号右边的数字，那就从第一个打印到第5个
print(astring[:4])
# 负数表示倒数，-3表示从最后往前数3个
print(astring[-3:])

strnumber = "965874123"
# The general form is [start:stop:step]，step表示步长
# 左包右不包！！！
# 现实应用，比如说 随机抽组
print(strnumber[3:7:2])
print(strnumber[3:7:3])

print(strnumber[::3])
print(strnumber[1::3])
print(strnumber[2::3])

# 反转走一遍！
astring = "Hello world!"
print(astring[::-1])

# 把里面的字符串，全部转为大写或者小写字母
astring = "Hello world!"
print(astring.upper())
print(astring.lower())
# 练习：最后一个字母要求大写
upper = astring[10]
print(astring[:-2] + upper.upper() + astring[11:])
print(astring[:-2] + astring[-2].upper() + astring[-1:])

# 判断字符串以什么开始、什么结尾
# startwith 表示判断，会true
astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))
# 或者
if astring.startswith("Hello"):
    print("true")
else:
    print("false")
# 如果忽略大小写，只看字母是否正确的写法：
low = astring.lower()
if low.startswith("hello"):
    print("true")
else:
    print("this is false")


# 先定义一个空的字符串，目的是存储每次循环的结果。
# 数学里的=是比较，程序里的==是比较。一个=是赋值
astring = "Hello world!"
x = ""
words = astring.split(" ")
print(words)
for oneword in words:
    first = oneword[0]
    word1 = first.upper() + oneword[1:]
    x = x + word1 + " "
print(x)
tmp = x[:-1]
print(tmp)
print(x[:-1])

# 练习：exercise
s = "Hey there! what should this string be?"
# e hr!wa hudti tige
# e hr!wa hudti tigb?
# Length should be 20
print("Length of s = %d" % len(s))

print("The first occurrence of the letter a = %d" % s.index("a"))

print("a occurs %d times" % s.count("a"))

print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The first five characters are '%s'" % s[0:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10

print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end
print("The last five characters are '%s'" % s[:-5]) # 5th-from-last to end

# 练习：exercise
s = "Hey there! what should this string be?"
print("String in uppercase: %s" % s.upper())
print("String in lowercase: %s" % s.lower())
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")
else:
    print("no")

if s.endswith("be?"):
    print("String ends with 'be?'. Good!")

print("Split the words of the string: %s" % s.split(" "))
# "Hey" "there!" "what" "should" "this" "string" "be?"




# 以下是自学廖雪峰的课程
# 2022.02.14 "数据类型和变量" complete

# 也可以打印整数，或者计算结果：
print(100+200)
# 可以把计算100 + 200的结果打印得更漂亮一点：
print("100 + 200 =", 100 + 200)

# input: 是与用户的简单交互。就是需要在下面输入名字，这个程序才会执行！
# name = input('please enter your name:')
# print('hello', name)

# exercise
a = -1
if a > 0:
    print("a is over 0")
else:
    print("a is no more than 0")

# Python可以处理任意大小的整数，很大的数，比如100000000000，很难数清有几个0，Python允许在数字中间以_分隔
# 举例：写成10_000_000_000, 和10000000000完全是一样的！

# 浮点数：要记住科学计数法，1.23x109和12.3x108是完全相等的， 10用e代替

# 转义字符\ 可以转义很多字符， 比如\n表示换行,字符\本身也要转义，所以\\表示的字符就是\
print('I\'m OK.')
print('I\'m learning\n Python.')
print('\\\n\\')
# 很多字符需要转化，要用很多\\\，为了简化，还可以用r'' 来表示默认字符串不转化
print(r'\\\t\\')
print(r'\\\n\\')
# 这表示要转
print('\\\n\\')

# 换行：除了\n, 还可以用'''...'''表示有多行内容
# 还可以加上r
print('''line1
...line2\n
line3''')

print(r'''line1
...line2
...line3''')

# 为什么不行？？？
name = 'vicky'
age = 77
gender = 'girl'
print('''name
...age''')

# 布尔值：一个布尔值只有True、False两种值，常用于条件判断中
age = 11
if age >= 18:
    print("adult")
else:
    print("teenager")

# 空值：空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

# 注意：请不要把赋值语句的等号等同于数学的等号
x = 10
x = x +1
# 重新赋值后，x = 11

# 题目：让hello world两个单词的第2个位置，全部变为大写
title = "hello world"
newtitle = title.split(" ")
print(newtitle)
x = ""
for oneword in newtitle:
    second = oneword[1]
    word1 = oneword[0] + second.upper() + oneword[2:]
    x = x + word1 + " "
print(x)
# 去掉最后一个空格
x1 = x[:-1]
print(x1)

# 再理解下=是赋值这件事情
a = 'ABC'
b = a
a = 'XYZ'
print(b)

# 常量：就是不能变的变量，比如常用的数学常数π就是一个常量
# 在Python中，通常用全部大写的变量名表示常量
PI = 3.14159265359

# 除法：有两种，一种是/，计算结果是浮点数（即使本来结果是整数，也会浮点）；一种是// 地板除，结果一定是整数
# 余数，用%
a = 11 / 3
b = 8 / 4
print(a, b)

a = 11 // 3
print(a)

b = 6 % 4
print(b)

# 练习
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print(s4)

