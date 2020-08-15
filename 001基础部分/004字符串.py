"""
字符串可以使用单引号'' 双引号"" 以及三引号 ''' '''(可以进行换行操作)

"""
# print('Hello World !')
# print("Let's go !")  # 防止与单引号冲突
# print('Let\'s go')  # 可以使用转义字符
# print('''Hello
# World''')  # 可以进行换行操作""""""也可以


"""
字符串的常用操作方法:
1.查找:
find:检测某个子串是否包含在这个字符串中
返回:(存在)子串开始位置的下标, (不存在)-1
语法:字符串序列.find(子串,开始位置下标,结束位置下标)

rfind() 和find函数功能相同，但查找方向与find的用法相反
index() 与find函数相同,子串不存在  报错
rindex() 与index用法相同， 方向相反

count() 用于查找给定字符串的出现次数
"""
str1 = 'Hello World'
str1.find('llo')
str1.index('llo')
str1.count('llo')


"""
字符串的修改:
replace():替换
字符串序列.replace(旧子串,新子串,替换次数)
返回值为修改后的字符串，原来的字符串不会被改变
替换次数超过子串出现次数，则替换全部
如果不提供替换次数则会替换全部的内容
"""
str1 = 'Hello World'
new_str1 = str1.replace('World', 'DaWang')

"""
split():分割数据，返回一个列表，会丢失分割字符
语法:
字符串序列.split(分割字符,分割次数)

"""

str1 = 'Hello World'
list1 = str1.split('o')

list1 = str1.split('o', 1)


""""
join():--合并列表中的字符串数据为一个大字符串数据
语法：连接符.join(列表) 返回一个字符串
"""
mylist = {'aa', 'bb', 'cc'}
str1 = '...'.join(mylist)
print(str1)
"""
capitalize()  将第一个字符转成大写
title() 将每个单词首字母转成大写
lower() 将大写转换成小写
upper() 将小写转换成大写

"""
str1 = 'hello world'
new_str1 = str1.capitalize()
"""
删除空白字符：
lstrip()  删除左侧空白字符
rstrip()  删除右侧空白字符
strip()  删除两侧空白字符
"""
'       hello    '.rstrip()
"""
字符串对齐：
ljust(对齐的字符长度,'填充字符')  左对齐
rjust(对齐的字符长度,'填充字符')  右对齐
center(对齐的字符长度,'填充字符')  中间对齐
"""
str1 = 'Hello World'
new_str1 = str1.ljust(50, '.')

"""
字符串的判断：
startswith():检查字符串是否以某一字符串开头
语法:
字符串序列.startswith(子串,开始位置下标，结束位置下标)   
endswith():检查字符串是否以某一字符串结尾
语法:
字符串序列.endswith(子串,开始位置下标，结束位置下标)   
"""
str1 = 'Hello World'
i = str1.startswith('Hello')

"""
isalpha():如果该字符串都是以字母组成则返回True，反之返回False 
isdigit():如果该字符串都是以数字组成则返回True，反之返回False 
isalnum():如果该字符串都是以字母或数字组成则返回True，反之返回False
isspace():如果该字符串都是空格则返回True，反之返回False  
"""
str1 = 'Hello World'
i = str1.isalpha()

