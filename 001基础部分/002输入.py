"""
输入基本语法 ：变量名 = input("提示信息")
在python3中input中返回的类型一律为'str'类型
"""
password = input("请输入您的密码：")
print(f"您输入的密码是：{password}")
print(type(password))
