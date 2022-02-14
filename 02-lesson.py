# append是指追加, list里，要放东西，必须加append
# 这样打印出来的字符串，打印出来，是有双引号或者单引号的；数字的话，就没有
eyeshadow = []
eyeshadow.append("Pink")
eyeshadow.append("Blue")
eyeshadow.append("Yellow")
eyeshadow.append("Green")
eyeshadow.append("Black")
eyeshadow.append("Purple")
print(eyeshadow)

# 在现实应用中，提取 就不带双引号
# 在计算机里，从0开始数数
print(eyeshadow[3])

# 现实应用
# 要先声明，再放东西
tabletitle = ['name', 'gender', 'age', 'address']
userinfo = []
userinfo.append("veekie")
userinfo.append("female")
userinfo.append("0")
userinfo.append("1")
print(tabletitle)
print(userinfo)


usernames = ["张阳冰", "张思", "张问芙", "张天纵", "张修敏", "张和韵", "张敏", "张希彤", "张晓枫", "张涵映", "张秀筠", "张棠华", "张恨真", "张运珊", "张怀桃"]
# for 循环
# 现实应用，利用循环来筛选
for info in usernames:
    if info.endswith("思") or len(info) == 2:
        print("结果: " + info)

for info in usernames:
    if len(info) == 2:
        info = info[0] + info[1]*2
        print("结果: " + info)

info = "张阳冰"
print(info[0])


# 以下是自学廖雪峰的课程

# 也可以打印整数，或者计算结果：
print(100+200)
# 可以把计算100 + 200的结果打印得更漂亮一点：
print("100 + 200 =", 100 + 200)

# input: 是与用户的简单交互。就是需要在下面输入名字，这个程序才会执行！
name = input('please enter your name:')
print('hello', name)

# exercise
a = -1
if a > 0:
    print("a is over 0")
else:
    print("a is no more than 0")






