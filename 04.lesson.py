# boolean: 布尔值，就是真假
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True
print(x != 4) #x不等于4

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





