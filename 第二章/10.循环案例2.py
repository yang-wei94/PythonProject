# """
#     案例2: 猜数字游戏
#          1. 系统随机生成一个随机数
#          2. 用户根据提示猜数字,并将所猜的数字输入系统
#          3. 如果猜错,系统给出提示是猜大了,还是猜小了
#          4. 如果猜对,系统自动退出,游戏结束
#
#
# """
# import random
# random_number = random.randint(1,100)  # 生成随机数
#
# while True:
#     num = int(input("请输入一个数字:"))
#
# #  比较
#     if num > random_number:
#         print("您输入的数大了.")
#     elif num < random_number:
#         print("您猜的数字小了.")
#     else:
#         print("真厉害,您猜对了!")
#         break
#
# print("随机生成的数字是:",random_number)


#    1-1000之间(含1000)所有的5的倍数的数字累加之和.
total = 0
for i in range(1,1001):
    if i % 5 == 0:
        total += i
print(f"1-1000之间所有5的倍数的数字之和是: {total}")


#统计字符串"akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"  字符串中有多少个a和k
total = 0
total2 = 0
msg = "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
for i in msg:
    if i == "a":
        total += 1
    elif i == "k":
        total2 += 1
print(f"字符串中有{total}个a和{total2}k.")
