"""
异常：
1.当检测到一个错误时，解释器就无法继续执行了，反而出现了一些错误的提示，这就是所谓的异常
2.异常的写法：
try:
  可能发生错误的代码
except:
  如果出现异常执行的代码
"""
try:
    open('test.txt', 'r')

except:
    open('test.txt', 'w')

"""
捕获指定异常:
语法：
try:
  可能发生错误的代码
except 异常类型:
  如果出现异常执行的代码
注意：
1.如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常
2.一般try下方只放一行代码
"""
# NameError
# print(num)
# ZeroDivisionError
# 1/0

try:
    print(num)
except NameError:
    print("有错误")
# 捕获多个指定的异常类型
try:
    1/0
except(NameError, ZeroDivisionError):
    print("有错误")

"""
捕获异常描述信息：

"""
try:
    print(num)
except(NameError, ZeroDivisionError) as result:
    print(result)

"""
捕获所有异常：
Exception是所有异常的父类
"""
try:
    print(num)
except Exception as result:
    print(result)

"""
异常中的else:
else表示的是如果没有异常要执行的代码 
当代码没有异常时try和else后面的代码都要去执行
"""
try:
    print(1)
except Exception as result:
    print(result)
else:
    print("没有异常")
"""
finally:无论是否异常都要执行的代码：


"""
try:
    f = open('test.txt', 'r')

except:
    f = open('test.txt', 'w')

finally:
    f.close()
    print("已经关闭文件")  # the file is closed

"""
自定义异常：
在python中，抛出自定义异常语法raise异常类对象。
"""
# 1.自定义异常类：
class ShortIputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    def __str__(self):
        return f'您输入的密码长度是{self.length},系统要求的最小长度为{self.min_len}'


def  main():
    try:
        con = input("请输入您的密码：")
        if len(con) < 3:
            raise ShortIputError(len(con), 3)
    except Exception  as result:
        print(result)

    else:
        print(f'您输入的密码是:{con}')


main()








