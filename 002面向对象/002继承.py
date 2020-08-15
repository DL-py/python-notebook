"""
继承：减少代码量
"""
"""
单继承:一个类只继承了一个父类
多继承：一个类同时继承了多个父类(默认使用第一个父类的同名属性和方法)
1.若子类重写父类的属性和方法，则默认调用子类
2.允许多层继承
"""


class Master(object):  # 父类1：Master
    def __init__(self):
        self.kongfu = '古法煎饼果子'

    def make_cake(self):
        super(Master, self).make_cake()
        super(Master, self).__init__()
        print(f'用{self.kongfu}制作煎饼')


class School(object):  # 父类2：School
    def __init__(self):
        self.kongfu = '新法煎饼果子'

    def make_cake(self):
        print(f'用{self.kongfu}制作煎饼')


class Learner1(School, Master):
    def __init__(self):
        self.kongfu = '独创方法'

    def make_cake(self):
        print(f'用{self.kongfu}制作煎饼')


"""
查询继承关系：类名.__mro__
"""
"""
子类调用父类的同名属性和方法：
要想调用父类的同名属性和方法，属性在init初始化位置，需要再次调用init
注意：此时调用自己的属性和方法也要在前面加上自己的初始化
"""


class Learner2(Master):
    def __init__(self):
        self.kongfu = '独创方法'

    def make_cake(self):
        self.__init__()
        print(f'用{self.kongfu}制作煎饼')

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)  # 子类调用父类


class Learner3(Learner2):
    pass


"""
利用super函数调用父类方法（一次性调用父类的方法）：
1.super带参数的写法：
super(当前类名,self).函数()
2.super无参数的写法：
super().函数()
"""

"""
私有属性和方法:在属性和方法名前面加入__
注意：
1.私有属性和方法不能继承给子类，且类外无法调用
2.可以用公有方法来访问私有属性
"""


class Learner4(Master, School):

    def __init__(self):
        self.kongfu = '独创方法'
        self.__money = 20000  # 私有属性

    def __info_print(self):  # 私有方法
        print(self.__money)
        print(self.kongfu)

    def make_cake(self):
        self.__init__()
        print(f'用{self.kongfu}制作煎饼')

    def make_master_cake(self):
        # 有参形式：
        super(Learner4, self).__init__()
        super(Learner4, self).make_cake()
        # 无参形式：
        # super().__init__()
        # super().make_cake()

    def set_money(self):
        self.__money = 500

    def get_money(self):
        return self.__money





