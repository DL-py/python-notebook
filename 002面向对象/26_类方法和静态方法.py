"""
类方法和静态方法：
注意：当出行同名的实例方法时，类方法和静态方法将失效
"""
"""
1.类方法
1.类方法：装饰器@classmethod修饰,一般使用cls作为第一个参数
2.实例化对象可以调用类方法，类本身也可以调用类方法。
3.类方法一般与类属性连用,用来访问私有的类属性
"""


class Dog(object):
    __tooth = 10

    @classmethod
    def get_tooth(cls):
        return cls.__tooth


WangCai = Dog()
Dog.get_tooth()
WangCai.get_tooth()
"""
2.静态方法：
1.静态方法：@staticmethod来修饰，既不需要传递类对象也不需要传递实例对象
2.静态方法可以通过实例对象和类对象去访问
3.取消不需要的参数传递，减少不必要的内存占用和性能消耗
"""


class Dog(object):
    @staticmethod
    def info_print():
        print("这是一个静态方法")


WangCai = Dog()
WangCai.info_print()
Dog.info_print()
