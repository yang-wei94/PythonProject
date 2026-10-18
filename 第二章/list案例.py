################
## 1.生成1-20的平方列表
## 2.从数字列表中提取所有偶数,并计算其平方,生成一个新列表
num_list = []
for num in range(1,21):
    num_list.append(num ** 2)
print("1-20的平方列表是:", num_list)

num_list2 = [i ** 2 for i in range(1,21)]
print("简化版1-20的平方列表:", num_list2)


s = [1, 55, 46, 15, 86, 102, 23, 75, 87, 60, 52, 61]
b = []
for num in s:
    if num % 2 == 0:
        b.append(num ** 2)
print("提取偶数后,生成平方后的新列表是:", b)

w = [i**2 for i in s if i % 2 ==0]
print("简化版取偶,生成平方新列表:", w)


"""
根据用户输入10个数字,并存储到列表中,顺便完成排序,
再输出最小值,最大值以及平均值
"""
num_list = []
for i in range(10):
    num = int(input("请输入您要存储的数字:"))
    num_list.append(num)

print("您新建的数据集是:", num_list)

num_list.sort()
print("列表排序之后的结果是:", num_list)

print("数据中最小值是:", num_list[0])
print("数据中最大值是:", num_list[-1])
print("整个数据集平均值是:", sum(num_list)/len(num_list))


########################
num_list1 = [23, 56, 96, 85, 169, 65, 15, 18, 36, 16]
num_list2 = [96, 18, 57, 100, 23, 36, 88, 56]
##合并列表的三种方法#######
for num in num_list1:
    num_list2.append(num)
print("合并之后的列表:", num_list2)

##############
num_list = num_list1 + num_list2
print("合并之后的列表:", num_list)

########
num_list = [*num_list1, *num_list2]
print("合并之后的列表:", num_list)

new_list = []
for num in num_list:
    if num not in new_list:
        new_list.append(num)
print("去重后的新列表:", new_list)


#将如下多个列表合并成一个列表,并去重重复元素,排好序(升序)后输出到控制台
list1 = ["M", "A", "C", "E", "F", "G", "H", "L", "N", "I", "J", "K", "O"]
list2 = ["X", "Z", "T", "Y", "D", "E", "F", "G"]
list3 = ["W", "A", "S", "D"]

##str_list = list1 + list2 + list3
str_list = [*list1, *list2, *list3]
print("合并后的列表是:", str_list)

list = []
for i in str_list:
    if i not in list:
        list.append(i)
print("合并完,去重后的列表为:", list)

list.sort()
print("排序后列表:", list)


"""
将如下列表中能被3 或 5 整除的元素提出来,并获取这些数字对应的平方,
组成一个新的列表.
"""
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

list = [i for i in range(1,31) if i % 3 == 0 or i % 5 == 0]
print("新列表:", list)

#####将如下列表中正数提取出来,封装为一个新的列表
list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
list = [i for i in list1 if i > 0]
print("新的列表:", list)
