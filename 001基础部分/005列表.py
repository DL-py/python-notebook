"""
列表:存储多个数据(可不同类型)
"""
name_list = ['Tom', 'Bob', 'Jack']
"""
一、添加数据：
1.append:结尾追加数据如果是序列则将序列整体加入
语法：列表序列.append(数据)
2.extent:结尾追加数据,主要用于将序列中的元素分别加入列表
语法：列表序列.extent(数据)
3.insert:指定位置新增数据
语法：列表序列.insert(位置下标，数据)
"""
name_list.append('Lily')
name_list.extend(['hello', 'world'])
name_list.insert(0, 'BBB')
""" 
总结：
1.append和insert用法类似，不同之处在于append在加在末尾，insert可以任意指定位置
2.extend主要使用与将序列中的元素加入末尾， 不能加入整型、浮点型数据
3.这些函数只是适用于列表类型的数据
"""

"""
二、逆序：
reverse:
语法：列表序列.reverse()
"""
list1 = [2, 1, 3, 4]
list1.reverse()

"""
三、排序操作：
sort:
语法：列表序列.sort(key=NoNe,reverse=False)
reverse表示排序规则，reverse=True降序，reverse=False升序(默认)
"""
list1.sort(reverse=True)





