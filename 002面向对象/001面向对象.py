"""
封装：
"""
"""
2.类的创建：
class 类名(object):
     代码
    ......
"""
"""
3.实例化对象：
对象名 = 类名()
"""
"""
4.对象属性的添加和获取：
1.类内:
添加：self.属性名
获取：属性名 = 值
2.类外：
添加：对象名.属性名 = 值
获取：对象名.属性名
"""
"""
5.魔法方法：具有特殊功能的函数
1.__init__()：初始化对象调用
2.__str__():打印对象时调用。
3.__del__():删除对象时调用
"""


class Washer(object):
    def __init__(self, height, width):
        self.width = width
        self.height = height

    def __str__(self):
        return "这是洗衣机的说明书"

    def __del__(self):
        print("该对象已经被删除")

    def wash(self):
        print("能洗衣服")
        print(f'洗衣机的宽度为{self.width},洗衣机的高度为{self.height}')
        print(self)







