# 面向对象编程

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

# Class是一种抽象概念，比如我们定义的Class——Student，是指学生这个概念，
# 而实例（Instance）则是一个个具体的Student，
# 比如，Bart Simpson和Lisa Simpson是两个具体的Student。




