"""
多态：继承相同的父类，重写父类的方法不同，可以产生多种类型的子类
"""


class Dog(object):  # 父类
    def work(self):
        pass


class ArmyDog(Dog):  # 子类1
    def work(self):
        print("追击敌人....")


class DrugDog(Dog):  # 子类2
    def work(self):
        print("追击毒品...")

















