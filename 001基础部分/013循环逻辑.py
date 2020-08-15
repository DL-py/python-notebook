"""
循环逻辑：
1.while:通过条件语句进行判断
2.for:生成一个可以迭代的序列
与c语言的区别是for和while均可以和else连用
break和continue的用法与c语言相同
"""
"""
while 条件:
         条件成立要执行的代码
         .......
"""
i = 0
while i < 5:  # 书写习惯
    print("媳妇，我错了")
    i += 1  # 不能使用i++
print("原谅你了")

# break 与 continue 的区别
# break 终止此循环
# continue 终止当前一次循环而执行下一次循环

k = 1
while k <= 5:
    print(f"我吃了{k}个苹果")
    if k == 3:
        print("我吃饱了！")
        break
    k += 1

k = 1
while k <= 5:
    if k == 3:
        print(f"第{k}个苹果有虫子")
        k += 1
        continue  # 如果使用continue 之前一定要修改计数器,否则会进入死循环
    print(f"我吃了第{k}个苹果")
    k += 1


# while循环的嵌套：
k = 1
i = 1
while k <= 3:
    while i <= 3:
        print("媳妇，我错了!")
        i += 1
    print("刷今天晚饭的碗")
    i = 1
    k += 1

"""
for 循环：语法：
   for 临时变量 in 序列:
             重复执行的代码
             .......
   
"""

str1 = 'itha'
for i in str1:
    if i == 'h':
        continue
    print(i)

"""
while...else...
while 条件:
     条件成立重复执行的代码
else 
     循环正常结束要执行的代码         
"""

# 当break 非正常结束时else下方的代码不会执行
k = 1
while k <= 5:
    if k == 3:
        print(f"第{k}个苹果有虫子")
        break
    print(f"我吃了第{k}个苹果")
    k += 1
else:
    print("循环结束")
# 当continue时else下方的代码会执行
k = 1
while k <= 5:
    if k == 3:
        print(f"第{k}个苹果有虫子")
        k += 1
        continue
    print(f"我吃了第{k}个苹果")
    k += 1
else:
    print("循环结束")

"""
for...else...
语法:
    for 临时变量 in 序列:
        重复执行的代码
        ......
    else:
        循环正常结束要执行的代码
        
"""
# 当break 非正常结束时else下方的代码不会执行
str1 = 'itha'
for i in str1:
    if i == 'h':
        break
    print(i)
else:
    print("循环结束")
# 当continue时else下方的代码会执行
str1 = 'itha'
for i in str1:
    if i == 'h':
        continue
    print(i)
else:
    print("循环结束")

"""
zip函数：将一系列可迭代类型的数据，如列表，中的数据打包成元组，然后返回一个zip对象
zip可迭代，但是不能直接打印，与range函数类似
"""
a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]
zipped = zip(a, b)     # 打包为元组的列表
[(1, 4), (2, 5), (3, 6)]
zip(a, c)              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
zip(*zipped)
# 与 zip 相反，*zipped 可理解为解压, 返回的是两个元组
# zip(*zipped)会返回zipped解压后的结果，zipped就会失效

