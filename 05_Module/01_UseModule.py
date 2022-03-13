# 使用模块

# 第1行和第2行是标准注释:
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释:
' a test module '

__author__ = 'Michael Liao'

# 以上就是Python模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错。
# 后面开始就是真正的代码部分:

import sys

# 这里相当于，让程序可以从外面选择运行那部分代码（给客户选择的机会）
def test():
    args = sys.argv                # 可以获取给的参数：01_UseModule/Edit/Parameter,这里可以修改自定义
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()





# 作用域:

# 有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的
# 前缀_的是只有本文件能够使用的

sys.warnoptions
sys._git


# __xxx__这样的变量是特殊变量
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；




