"""
输出总结：
1.常量的输出：print(常量)
2.有变量的输出：print(变量)
多个常量和变量输出用逗号隔开
3.在字符串中输出输出变量
3.1print('我的年龄是%d', age)
3.2print(f'我的年龄是{age}')
3.3print('我的年龄是{}'.format(age))
4.对于整型数据可以自定义位长%0nd, 对于浮点型数据可以限制小数点后面的位数%.3f
5.可以输出转义字符以及可以自定义结尾
"""
# 1.仅字符串的输出：
print("Hello World !")

# 整型数据输出 %d

age = 18
print(age)  # 可以直接输出变量

print("我的年龄是:%d" % age)


# 浮点数输出 %f(默认精确到小数点后六位)
weight = 75.5
print("我的体重是：%.2f" % weight)  # 精确到小数点后两位

# 字符串数据输出 %s
name = "Tom"
print("我的名字是:%s" % name)

# 输出域宽设置  %nd 不足补0超出原样输出
stu_id = 1
print("我的学号是：%03d" % stu_id)  # 如果3前面不加0则默认是补空格

# 字符串输出的拓展用法
print("我的名字是：%s,我的年龄是%s岁，我的体重是：%s公斤" % (name, age, weight))

# f格式化字符串 f'{表达式}'两种格式都可以
print(f"我的名字是：{name},今年{age},体重是{weight}公斤")
print('我的名字是：{},今年{}, 体重是{}公斤'.format(name, age, weight))

# 转义字符 换行\n  制表符 \t
print("Hello \nWorld")
print("Hello \tWorld")

# 结束符  print("Hello",end="\n")
print("Hello", end="\n")
print("Hello", end="\t")
print("World", end="\n")
print("Hello", end="...")  # 结束符可以用户自行设计
