# Python内置了字典：dict的支持，dict全称dictionary
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# 这种key-value存储方式，在放进去的时候，必须根据key算出value的存放位置，这样，取的时候才能根据key直接拿到value

# 改变key值
d['Adam'] = 67
print(d['Adam'])
d['Adam'] = 71
print(d['Adam'])

# 如果key不存在，dict就会报错
# d['Thomas']

# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print('Thomas' in d)                      # False
# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('Thomas'))                    # 返回none
print(d.get('Thomas', -1))                # 返回指定的默认值

# 删除一个key，用pop(key)方法，对应的value也会从dict中删除
# 同样，不能删除没有的key
print(d.pop('Bob'))

# dict内部存放的顺序，和key放入的顺序是没有关系的，他有自己的顺序

# 哈希算法Hash: 一种加密算法，保证在Dict里的key对应的对象是唯一的（加密过

# SET: set和dict类似，也是一组key的集合，但不存储value
s = set([1, 2, 3])
print(s)
s = set([1, 1, 2, 2, 3, 3])     # set的好处就是帮你去重复。因为不像dict，不会记下后面的value
print(s)

# add(key)
s.add(4)
s.add(1)                       # 如果加入重复的1，打印出来也不会重复
s.add('1')
print(s)
# remove(key)
s.remove(4)
print(s)

# set可以看成数学意义上的无序和无重复元素的集合, 因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)               # 交集
s1 | s2                      # 并集
print(s1 | s2)

# 再议不可变对象
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
s = set([1, 2, 3])
tuple1 = (1, 2, 3)
tuple2 = (1, [2, 3])

s.add(tuple1)               # set只能放不能变的东西，set是只有key的dict
print(s)

d[3] = tuple2
print(d)
d[1] = tuple1
print(d)
d[tuple1] = tuple1         # dict里，key不能变（所以能放tuple1），但是value可以变
print(d)
