# 递归函数:在函数里调用自己
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)


def fact_my(n):
    s = 1
    while n > 1:
        s = s * n
        n = n - 1
    return (s)

print("-------")
# print(fact_my(4))

#     sum = 1
#     for x in n:
#         if x > 0:
#             pass
#         sum = sum * x
#         n = n - 1
#         return sum
# print(fact_my(3))




# print(fact(1))
# print(fact(2))
print(fact(3))













