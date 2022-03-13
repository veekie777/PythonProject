# 类和实例
# 面向对象最重要的概念就是类（Class）和实例（Instance）

# 定义类是通过class关键字：
class Student(object):
    pass
# class后面紧接着是类名，即Student，类名通常是大写开头的单词，
# 紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，
# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。

# 定义好了Student类，就可以根据Student类创建出Student的实例，
# 创建实例是通过类名+()实现的：
bart = Student()
print(bart)
bart.name = "Veekie"
bart.age = 18
print(bart.name)

# 由于类可以起到模板的作用，
# 因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
# that is, 一个类里，进来一个学生，就强制告诉他的名字和分数
class Student(object):
    # 注意到__init__方法的第一个参数永远是self，表示创建的实例本身
    def __init__(self, name, score):     # 注意：特殊方法“__init__”前后分别有两个下划线！！！
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


bart = Student('Veekie', 18)

print('%s: %s' % (bart.name, bart.score))   # 方法一
bart.print_score()                          # 方法二：数据封装后


# 数据封装
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):                  # 封装 获得分数
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):                    # 封装 获得级别
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Veekie', 60)
bart.print_score()
print(bart.get_grade())

# 这样一来，我们从外部看Student类，就只需要知道，
# 创建实例需要给出name和score，而如何打印，都是在Student类的内部定义的，
# 这些数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节。


# 封装的另一个好处是可以给Student类增加新的方法，比如get_grade：




