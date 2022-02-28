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


# 求素数
su = [1, 2, 4, 5, 6, 7, 9, 10, 11, 13 ,14, 15]
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






