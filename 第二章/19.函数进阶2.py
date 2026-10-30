# # 函数的参数类型
# # 加
# from multiprocessing.sharedctypes import class_cache
#
#
# def add(x,y):
#     return x+y
# # 减
# def subtract(x,y):
#     return x-y
# # 乘
# def multiply(x,y):
#     return x*y
# # 除
# def divide(x,y):
#     return x/y
#
# # 计算
# def calc(x,y,oper):
#     return oper(x,y)
#
# calc(10,20,add)
#
# print(calc(10,20,add))
# print(calc(10,20,subtract))


# 匿名函数
# 需求 1. 打印一个分割线
def out_line():
    print("------------------")

out_line = lambda : print("-----------------------")

out_line()

# 需求 2. 计算两个数之和
def add(x,y):
    return x + y

add = lambda x,y: x + y
print(add(10,20))

# 需求 3. 完成如下列表的排序操作,按照每一个元素的字符个数,从小到大排序;
data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
data_list.sort(key= lambda item: len(item), reverse=True)
print(data_list)

#---------------------------------------案例--------------------------------------------------
# 案例1: 计算N的阶乘
# 定义一个函数,根据传入的数字,计算该数字阶乘的结果(阶乘公式: f(n) = n * f(n-1)
# 递归调用: 指的是在函数中,自己调用自己的情况------> 一定得有终结点
"""
jc(10) = 10 * jc(9)
jc(9) = 9 * jc(8)
jc(8) = 8 * jc(7)
jc(7) = 7 * jc(6)= 7 * 720 = 5040
jc(6) = 6 * jc(5)= 6 * 120 = 720
jc(5) = 5 * jc(4)= 5 * 24 = 120
jc(4) = 4 * jc(3)= 4 * 6 = 24
jc(3) = 3 * jc(2)= 3 * 2 = 6
jc(2) = 2 * jc(1)= 2 * 1 = 2
jc(1) = 1
"""
def jc(n):
    if n == 1:
        return 1
    else:
        return n * jc(n-1)

result = jc(10)
print(result)



