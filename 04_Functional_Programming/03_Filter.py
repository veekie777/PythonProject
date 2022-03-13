# Python内建的filter()函数用于过滤序列
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(L)

L = list(map(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(L)


# 把一个序列中的空字符串删掉

def not_empty(s):
    return s and s.strip()

L = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(L)

print('  kjlkj lkjlkj '.strip())

# string.strip函数讲解：https://blog.csdn.net/csdn15698845876/article/details/73469234
# 如果strip()的参数为空，那么会默认删除字符串头和尾的空白字符(包括\n，\r，\t这些)
# 或者要删除首尾的某些元素：print(a.strip('abs')
# lstrip()和rstrip(), 一个是去掉左边的(头部)，一个是去掉右边的(尾部)


# 求素数
su = [1, 2, 4, 5, 6, 7, 9, 10, 11, 13, 14, 15]
def sushu(s):
    a = []
    for x in s:
        if x > 0:
            if x == 1:
                a.append(x)
            else:
                count = 0
                dividend = 1
                while dividend <= x:
                    if x % dividend == 0:
                        count = count + 1
                    dividend = dividend + 1
                if count == 2:
                    a.append(x)
    return a

L = list(sushu(su))
print(L)





def sushu(x):
        if x == 1:
            return True

        count = 0
        dividend = 1
        while dividend <= x:
            if x % dividend == 0:
                count = count + 1
            dividend = dividend + 1
        if count == 2:
            return True
        else:
            return False

L = list(filter(sushu, su))
print(L)

# 1.要大于0
# 2.1是素数
# 3.大于1的素数，只能被1和自己整除


# 练习（1）：
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。
# 请利用filter()筛选出回数
def number(x):
    x = str(x)
    if len(x) % 2 == 1:
        count = (len(x) - 1) / 2
    else:
        count = len(x) / 2
    endn = len(x) - 1
    pren = len(x) - 1 - endn

    # if endn > 1 and len(x) % 2 == 1:
    while count > 0:
        if x[pren] != x[endn]:
            return False
        endn = endn - 1
        pren = pren + 1
        count = count - 1
    return True


x = [12321, 11, 523, 525, 7, 11111548484361]
L = list(filter(number, x))
print(L)



L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L))                     # 对key进行排序
print(list(reversed(sorted(L))))     # 反排序
# 按照成绩大小排  ????








