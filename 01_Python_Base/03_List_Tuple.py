# list
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)               # ['Michael', 'Bob', 'Tracy']

# list排序
classmates.sort()               # 按照公认的顺序进行排序
print(classmates)


# 获得list长度
len(classmates)                # 3

# 用索引来访问list中每一个位置的元素，记得索引是从0开始的
classmates[0]                  # 'Michael'
classmates[-1]                 # 获取倒数第一个

# List 中追加元素
classmates.append('Adam')      # 在最后追加

# List 中插入元素
classmates.insert(1, 'Jack')   # ['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']

# LIst中,pop没写数字就删除最后一个元素，并获取
x = classmates.pop()           # ['Michael', 'Jack', 'Bob', 'Tracy']
# pop不光删除，还赋值。此时x的值就是'Adam'

# 替换list中某位置的值
classmates[1] = 'Sarah'        #  ['Michael', 'Sarah', 'Tracy']



# Tuple: 元组,tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')
classmates[0]
# 定义空tuple
t = ()
# 定义一个tuple，为了和数学()区分，加了一个,
t = (1,)
