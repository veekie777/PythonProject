# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 取前三个元素, 左包右不包
print(L[0:3])
print(L[:])
print(L[:3])
print(L[2:])
print(L[:-1])
print(L[-2:])
print(L[::2])          # 每两个取一个

# Tuple也可以切，字符串也可以切
T = (0, 1, 2, 3, 4, 5)
print(T[:3])

s = 'ABCDEFG'
print(s[2:4])


# 练习

# 去掉所有空格
def trim(s):
    idx = 0
    for space in s:
        if space == " ":
            s = s[0:idx] + s[idx+1:]
        else:
            idx = idx + 1
    return s

print(trim('  12  54  64165  '))





# 去掉首尾的空格
def trim1(d):
    if len(d) == 0:
        return d

    while len(d) > 0:
        if d[0] == " ":
            d = d[1:]
            continue
        elif d[-1] == " ":
            d = d[:-1]
            continue
        return d


print("=======")
print("1="+trim1('  1  54    64165  '))
print("2="+trim1('1  54    64165   '))
print("3="+trim1('  1  54    64165'))
print("4="+trim1('  1  54    64165'))
print("5="+trim1(''))





