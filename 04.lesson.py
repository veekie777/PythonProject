# boolean: 布尔值，就是真假
x = 2
print(x == 2)   # prints out True
print(x == 3)   # prints out False
print(x < 3)    # prints out True
print(x != 4)   # x不等于4

# Boolean operators 布尔操作符
name = "John"
age = 23
name2 = 'Tom'
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

if name == 'John' and age == 35 or name2 == 'Tom':
    print("3")

if (name == 'John' and age == 35) or (name2 == 'Tom'):
    print("3")

# if 判断
# 这三种只进一种
statement = False
another_statement = True
if statement is True:
    print(1)
    pass   # pass是空语句，只是为了占位置，不然if后面不做什么、就会报错
elif another_statement is True: # else if
    print(2)
    pass
else:
    print(3)
    pass
print(4)

# 在Python里面，除了false是假，以下情况都是假“false”
# An empty string: "" 2. An empty list: [] 3. The number zero: 0
# "" [] is 都是 False
boolean = True
strEmpty = ""
listEmpty = []
x = [1, 2, 3]
y = [1, 2, 3]

if boolean:
    print("boolean is True")

if strEmpty:
    print("strEmpty is True")
else:
    print("strEmpty is False")

if listEmpty:
    print("listEmpty is True")
else:
    print("listEmpty is False")

# x和y内容一样，所以第一个true，第二个false
print(x == y)
print(x is y)


flag = "John"
flag = "lll" + "John"
flag = name == "John"

# not boolean：反转布尔值
# if后面居然还可以加not, 是上面那种情况的简便写法
if not strEmpty:
    print("strEmpty is not null")


# exercise
# change this code
number = 16
second_number = 0
first_array = [1]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

first_array = [1]
second_array = [1,2,3,4]
if len(first_array) + len(second_array) == 5:
    print("4")

first_array = [1]
if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")


# 以下是自学廖雪峰的课程：2022.02.15
# 《字符串和编码》
print('this is my self-learning note for 2022.02.15')

# string formatting 字符串格式化,第一种用%当作占位符
print('hello, %s, your mobile phone number %d is invalid now, please check your mother %s phone, thanks' % ('Lilei', 192837, 'Wangyi'))

print('my salary is %.2f' % 2323.564654)     # 浮点数2位
print('%2d - %02d' % (3, 1))                 # 原来整数前面也可以加东西，可以指定是否补0和整数与小数的位数

# %s永远起作用，它会把任何数据类型转换为字符串
print('age: %s, gender: %s' % (11, 'female'))

# 和\一样，当%是普通字符时，就用%%来转义
print('the percent of girls number is %.2f%%' % 23.4546)

# format(): 另一种格式化字符串的方法,占位符{0}、{1}, 不过这种方式写起来比%要麻烦得多：
print('hello, {0}, your grade increases {1:.1f}% '.format('Tom', 13.4646))

# f-string: 最后一种，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换：
r = 2.5
s = 3.14 * r ** 2
print(f'the area of a circle with radius {r} is {s:.2f}')

# exercise： 练习
# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，
#  并用字符串格式化显示出'xx.x%'，只保留小数点后1位：

# solution 1, %:
lastyear = 72
thisyear = 85
percent = (thisyear - lastyear) / lastyear * 100
print('Tom\'s grade increases %.1f%% this year' % percent)

# solution 2, format():
print('hello, {0}, your grade increases {1:.1f}% this year' .format('Tom', 18.136))

# solution 3, f-string:
print(f'Tom\'s grade increases {percent:.1f}%, last year is {lastyear}')



# 《使用list和tuple》

# list: list是一种有序的集合，可以随时添加和删除其中的元素
# list打印出来，会打印方括号和引号
classmates = ['Tom', 'John', 'Jacky']
print(classmates)
classmates.append('Alex')        # list是有序数列，可以用append追加
print(classmates)
print(len(classmates))           # 数一数长度
print(classmates[1])             # 找出list里的某个位置
print(classmates[-1])            # list可以倒着数，但是由于没有-0，所以list里倒着数，从1开始
classmates.insert(1, 'Jerry')    # 在list某个位置插入
print(classmates)
classmates.pop(1)                # 用pop删除某个位置的元素,拿出来后还可以继续用
print(classmates)
classmates.index('Tom')          # index:找到在哪一个位置
print(classmates)
classmates[1] = 'Sarah'          # 在某个位置替换
print(classmates)
s = [123, 'Me', 'smile', True]   # list里可以放不同类型的元素
print(s)
s1 = [22, 'love', True, [2, 4]]  # list里也可以放list
print(s1)
print(len(s1))
L = []
print(len(L))                    # 空list，长度是0


# tuple： 元组， tuple和list非常类似，但是tuple一旦初始化就不能修改
# 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。
# 如果可能，能用tuple代替list就尽量用tuple。
classmates = ('Tom', 'Jerry', 'Sarah')
print(classmates)                   # tuple不能append，不能insert
print(classmates[0])                # tuple里，也可找位置
print(classmates.index('Jerry'))    # tuple里找位置

# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
boys = ('Tom', 'Jerry', 'Alex')
print(boys)

s = ()                             # 定义一个空的tuple
print(s)
# 但是，当tuple只定义1个元素时，如果这么定义：
t = (1)
print(t)                           # 有歧义，既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义
# 因此，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t = (1,)
print(t)

# 那么，怎么让tuple可变？
s = [1, 2, 3]
t = ('a', 'b', s, ['Alex', 'Jerry'], 123)
print(t)                           # tuple虽然不可变，但里面可以放list

s.insert(3, 'He')
t = ('a', 'b', s, ['Alex', 'Jerry'], 123)
print(t)                           # 在s的list里改变元素，其实tuple的元素是没变的！

# exercise: 练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 练习1： 打印Apple
s1 = L[0]
A1 = s1[0]
print(A1)

# 练习2: 打印Python
s2 = L[1]
A2 = s2[1]
print(A2)

# 练习3: 打印Lisa
s3 = L[2]
A3 = s3[2]
print(A3)



# 以下是自学廖雪峰的课程：2022.02.16
print('this is my self-learning note for 2022.02.16')
# 《条件判断》

# if else
age = 11
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('teenager')
# 用elif做更细致的判断.可以有多个elif
age = 5
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
# if还可以简写
x = 3
if x:
    print('True')              # 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
else:
    print('no')

# input 让程序变得有意思
# t = input('birth: ')           # input返回的是str，不能和整数比较
# birthyear = int(t)             # 所以要先把str变成整数int
# if birthyear >= 1990:
#     print('90后')
# else:
#     print('90前')


# 练习：
# 小明身高1.75，体重80.5kg。
# 根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# 用if-elif判断并打印结果：

height = 1.75
weight = 85
BMI = weight / (height ** 2)
if BMI <= 18.5:
    print('过轻')
elif 18.5 < BMI <= 25:
    print('正常')
elif 25 < BMI <= 28:
    print('过重')
elif 28 < BMI <= 32:
    print('肥胖')
elif BMI > 32:
    print('严重肥胖')









