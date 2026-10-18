# # 列表操作
# # 定义
# s = [56, 90, 88, 65, 90, "A", "Hello", True]
#
# print(type(s))
# print(isinstance(s, list),)
#
# # 访问列表元素
# # 获取
# print(s[0]) # 正向索引 从0开始
# print(s[-8]) # 反向索引 从-1开始
#
# print(s[2])
# print(s[-6])
#
# # 修改
# s[5] = "ABC"
# print(s)
#
# # # 注意:如果指定的索引超出范围,将会报错
# # s[10] = "DEF"
# # print(s)
#
# # 删除
# del s[6]
# print(s)
#
# # 遍历
# for item in s:
#     print(item)


#--------------------------列表 list 切片-----------------------------
#定义列表
s = ["A", "C", "H", "K", "L", "B", "D", "X", "C", "U"]

# 切片操作: s[开始索引:结束索引:步长]
print(s[0:5:1])
print(type(s[0:5:1]))


print(s[:5:1])
print(s[:5:])
print(s[:5])

print(s[0:5:2])
print(s[0:-2:1])


#---------------------------------------------列表 list 常用方法---------------------------------------------
#列表定义
s = [56, 90, 88, 65, 90, 100, 209, 72, 145]
print(s)

# append(): 在列表尾部追加元素
s.append(188)
print(s)

# insert(): 在指定索引之前,插入元素
s.insert(2,80)
print(s)

# remove():  移除列表中第一个匹配到的元素
s.remove(90)
print(s)

# pop(): 删除列表中指定索引位置的元素并返回(如果未指定,默认删除最后一个)
e = s.pop(1)
print(e)

e = s.pop()
print(e)

print(s)

# sort(): 排序
s.sort()
print(s)

# reverse(): 反转列表元素
s.reverse()
print(s)


#---------------------------------------列表   list  案例----------------------------------
# 案例1. 将用户输入的10个数字,存储到一个列表中,并将列表中的数字进行排序,输出其中最小值 , 最大值 和 平均值

#  1.定义列表
num_list = []


# 2. 将用户输入的10个数字存入列表
for i in range(10):
    number = int(input("请输入一个有效数字:"))
    num_list.append(number)
print("数字列表:", num_list)


# 3. 排序
num_list.sort()
print("排序后的数字列表:", num_list)

#  4. 输出其中的最小值, 最大值 和 平均值  ----->sum():  求和  ;   len()  获取元素的个数(列表的长度)
print("最小值:", num_list[0])
print("最大值:", num_list[-1])
print("平均值:", sum(num_list)/len(num_list))




