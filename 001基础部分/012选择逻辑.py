"""
if...else...语法：
if 条件:
      条件成立执行的代码1
      条件成立执行的代码2
      ......
else:
      条件不成立执行的代码1
      ......
"""

if True:
    print("Hello World")  # 没有缩进的语句块与if条件语句不相关
print("OK")

# 实例1：
age = input("请输入您的年龄：")
if int(age) > 18:
    print("您已经成年")
else:
    print("您还未成年！")


"""
多重判断语法：
if 条件1:
      条件成立执行的代码1
      条件成立执行的代码2
      ......
elif 条件2:
     条件成立执行的代码1
     条件成立执行的代码2
     ......
else:
      条件不成立执行的代码1
      ......
"""
age = input("请输入您的年龄：")
if int(age) <= 18:
    print("您的年龄是：%s，童工" %age)
elif int(age) >= 60:
    print("您的年龄是：%s,已退休" % age)
else:
    print("您的年龄是：%s" % age)

# 化简  age >=18 and age <= 60   可以化简为 18 <=age <=60
"""
if 的嵌套
if 条件1:
        条件成立执行的代码
   if 条件2:
        条件成立执行的代码
        ......
"""





