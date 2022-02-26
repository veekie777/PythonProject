# 迭代器
# 可以使用isinstance()判断一个对象是否是Iterable对象：
from collections.abc import Iterable
isinstance([], Iterable)
True
isinstance({}, Iterable)
True
isinstance('abc', Iterable)
True
isinstance((x for x in range(10)), Iterable)
True
isinstance(100, Iterable)
False


# Iterable: 可以用for...in
# Iterator: 可以用for...in，还可以用next()














