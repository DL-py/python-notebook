"""
推导式：(本质上是一个简化了的for循环)
用处：用于生成符合特定规律的列表、字典和集合
"""
# 用法1：
"""
列表推导式：
"""
list1 = [i for i in range(10)]
list1 = [i for i in range(10) if i % 2 == 0]
list1 = [(i, j) for i in range(1, 3) for j in range(3)]
"""
集合推导式：
"""
set1 = {i**2 for i in list1}
"""
字典推导式:
1.快速建立一个有规律的字典
2.快速合并列表为字典或提取字典中目标数据
3.提取字典中的目标数据
"""
# 快速建立一个有规律的字典
dict1 = {i: i**2 for i in range(1, 5)}

# 快速合并列表为字典或提取字典中目标数据
list1 = ['name', 'age', 'gender']
list2 = ['Tom',  20,  '男']
dict1 = {list1[i]: list2[i] for i in range(len(list1))}

# 提取字典中的目标数据
counts = {'MBP': 201, 'HP': 125, 'Dell': 128}
count1 = {key: value for key, value in counts.items() if value >=200}





