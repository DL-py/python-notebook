# 创建字典：
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
dict2 = {}  # 空字典
dict3 = dict()

# get:获得某一键值
# 字典序列.get(key,默认值)
# 注意：如果当前查找的key不存在则返回默认值，如果省略第二个参数则返回None
dict1.get('age')
dict1.get('id', 1)

# keys()：返回所有key,组成可迭代对象
dict1.keys()

# values():返回所有values, 组成可迭代对象
dict1.values()

# items():返回所有所有的键值对，组成可迭代对象
dict1.items()

# 字典拆包：
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
for key, value in dict1.items():
    print(f'{key} = {value}')