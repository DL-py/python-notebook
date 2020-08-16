"""
文件操作：
*所有的读和写都是在光标后面进行*
https://www.runoob.com/python3/python3-func-open.html
*str类型与bytes类型的转换：
https://www.cnblogs.com/shengulong/p/11079291.html
"""
import os
import shutil

"""
1.打开文件：open()
2.读取文件：
read(num):num表示读取的字节数
readlines(num):按行读取，返回一个列表，每个元素是一行，用于for
readline(num):num表示读取的字节数
3.写入操作：write()
4.关闭文件：close()
"""
"""
移动指针的位置：
文件对象.seek(偏移量，起始位置)
起始位置：
0：文件开头
1：当前位置
2：文件结尾
1,2只适用于以二进制格式打开文件
"""
"""
文件与文件夹：
文件操作：
1.重命名：os.rename(旧名, 新名)
2.删除：os.remove(name)
文件夹操作：
*.创建文件夹:os.mkdir(name)
*.删除文件夹:os.rmdir(name)  # 当文件夹不为空时则无法删除
*.删除文件夹及其子文件：shutil.rmtree(path)
*.获得当前文件的目录:os.getcwd()
*.改变默认目录:os.chdir(源目录)
*.获取目录列表：os.listdir(目标)
*.重命名文件夹os.rename(旧名, 新名)
"""



























