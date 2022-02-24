# Unicode 可以表示全世界的语言（不分国别）
# 最新的Python 3版本中，字符串是以Unicode编码的
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
# ord是获取在Unicode中的编码
ord('A')                # 65
ord('中')                # 20013
# 根据Unicode的编码，获取对应的字
chr(66)                 # 'B'
chr(25991)              # '文'
# 还可以用十六进制这么写str
print('\u4e2d\u6587')   # 打印“中文”


# 字符串的replace方法
a = 'abc'
print(a.replace('a', 'A'))         # 一次性的，不会改变原来的旧值
print(a)
# 除非：
a = 'abc'
a = a.replace('a', 'A')
print(a)

# 字符串格式化：string format
# %d	整数
# %f	浮点数
# %.nf	浮点数（保留小数 四舍五入
# %s	字符串
# %x	十六进制整数

# 方法一（%）：
print('Hello, %s' % 'world')
print('%.2f' % 3.1415926)

# 方法二（format()）：
# 使用占位符{0}、{1}……
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

# 方法三（f-string）：
# 字符串如果包含{xxx}，就会以对应的变量替换
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')


x = list(range(1, 11))
print(x)

x = list(range(11))
print(x)


