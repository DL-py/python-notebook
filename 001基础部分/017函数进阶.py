"""
函数进阶：把函数作为参数传入，这样的函数成为高阶函数，高阶函数是函数式编程的体现。
函数式编程就是指这种高度抽象的编程范式。
函数式编程大量使用函数，减少了代码的重复，因此程序比较短，开发比较快

"""
"""
内置高阶函数：
1.map(func,lst):函数变量func作用于lst变量的每个元素中，并将结果组成迭代器返回
2.reduce(func,lst):其中func必须有两个参数
每个func计算的结果继续和序列的下一个元素做累积计算,使用时要导入functools
3.filter(func,lst):过滤序列，过滤掉(条件由func决定)不符合条件的元素，返回一个filter对象
"""

