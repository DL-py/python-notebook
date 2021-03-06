"""
函数：
"""
"""
函数定义：
def 函数名(参数):
    代码
"""
"""
函数的说明文档：
1.定义函数说明文档的语法：
def 函数名(参数):
 """    """内部写函数信息
  代码
2.查看函数的说明文档方法:
help(函数名)
"""


# 函数说明文档的高级使用：
def sum_num3(a, b):
    """
    求和函数sum_num3
    :param a:参数1
    :param b:函数2
    :return:返回值
    """
    return a + b


"""
返回值：可以返回多个值（默认是元组），也可以返回列表、字典、集合等
"""

"""
函数的参数：
1.位置参数：调用函数时根据函数定义的参数位置来传递参数
注意：传递和定义参数的顺序和个数必须一致
2.关键字参数：函数调用时，通过“键=值”形式加以指定，无先后顺序
注意：如果有位置参数时，位置参数必须在关键字参数的前面，但关键字参数之间不存在先后顺序
3.缺省参数（默认参数）：用于定义函数，为参数提供默认值，调用时可不传入该默认参数的值。
注意:所有位置参数必须出现在默认参数前，包括函数定义和调用
"""

"""
不定长参数：
不定长参数也叫可变参数，用于不确定调用的时候会传递多少个参数（不传参数也可以）的场景，
此时可以用包裹位置参数，或包裹关键字参数，来进行参数传递，会显得非常方便。
包裹位置传递：*args
args是元组类型，则就是包裹位置传递
包裹关键字传递：**kwargs
"""
