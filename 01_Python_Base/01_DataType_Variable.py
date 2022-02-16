# 整数
i = 1
i = 10_000_000_000

# 浮点数
f = 1.2356
# 一个数字的9次方的科学计数法
f = 1.23e9
# 科学计数法,0.000012
f = 1.2e-5

# 字符串
str = 'abc'
str = "abd"
# 字符串转义
str = 'I\'m \"OK\"!'
print('I\'m learning\nPython.')
print('\\\n\\')

# r开头的字符串，不进行转义
print(r'\\\t\\')

# '''字符串，可以换行，所见即所得
print('''line1
line2
line3''')

# r开头的'''字符串，不进行转义
print(r'''hello,\n
world''')

# 布尔值
print(True and True)       # True
print(True and False)      # False
print(False and False)     # False
print(5 > 3 and 2 > 1)     # True

print(not True)            # False
print(not False)           # True
print(not 1 > 2)           # True

# 空值: None不能理解为0，因为0是有意义的，而None是一个特殊的空值
None

# 变量指向：=是赋值，不是数学意义上的等号
a = 'ABC'
b = a
a = 'XYZ'
print(b)

a = [1, 2, 3]
b = a
a = [4, 5, 6]
print(b)




