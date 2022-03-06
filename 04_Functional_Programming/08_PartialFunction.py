# 偏函数
# 10进制变2进制
def int2(x, base=2):
    return int(x, base)

# 对比：
import functools
int2 = functools.partial(int, base=2)   # 原来是10进制，这里强行把默认值改了

# functools.partial的作用就是，把一个函数的某些参数给固定住
# （也就是设置默认值），返回一个新的函数，调用这个新函数会更简单












