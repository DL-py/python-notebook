"""
数据格式转换：

"""
# 转换为整型：int(变量名)
st = '10'
print(int(st))

# 转换为浮点型：float(变量名)
print(float(st))

# 字符串类型：str(变量名)
num = 1
print(str(num))

# 元组类型：tuple(变量名)
list1 = {10, 20, 30}
print(tuple(list1))

# 列表类型：list(变量名)
t1 = (10, 20, 30)
print(list(t1))

# eval()  执行一个字符串表达式，并返回字符串内的表达式的值(万能的)
str2 = '1'
print(eval(str2))
str4 = '{1000,2000,3000}'
print(eval(str4))
result = eval('str2*5')



