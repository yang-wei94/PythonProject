#  嵌套循环: 打印99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j} x {i} = {j * i}" , end = "    ")
    print()











# """
# 根据输入的直角边的边长，打印等腰三角形（如下为直角边为5的等腰直角三角形）
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# """
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()
#
#
# """
# 根据相应的数字，打印数字金字塔：
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# """
# for i in range(1, 7):
#     for j in range(1, i + 1):
#         print(f"{j}", end=" ")
#     print()
#
#
#
#
# """
# 需求3：打印国际象棋棋盘
# ■   □   ■   □   ■   □   ■   □
# □   ■   □   ■   □   ■   □   ■
# ■   □   ■   □   ■   □   ■   □
# □   ■   □   ■   □   ■   □   ■
# ■   □   ■   □   ■   □   ■   □
# □   ■   □   ■   □   ■   □   ■
# ■   □   ■   □   ■   □   ■   □
# □   ■   □   ■   □   ■   □   ■
# """
# # for i in range(1, 9):
# #     if i % 2 != 0:
# #         for j in range(1, 9):
# #             if j % 2 != 0:
# #                 print("█", end=" ")
# #             else:
# #                 print("□", end=" ")
# #         print()
# #     else:
# #         for j in range(1, 9):
# #             if j % 2 != 0:
# #                 print("□", end=" ")
# #             else:
# #                 print("█", end=" ")
# #         print()
#
#
# for i in range(8):
#     for j in range(8):
#         if (i + j) % 2 == 0:
#             print("■", end="  ")
#         else:
#             print("□", end="  ")
#     print()



"""
根据输入的直角边的边长，打印等腰三角形（如下为直角边为5的等腰直角三角形）

* * * * * 
* * * *
* * *
* * 
* 

"""
for i in range (5,0,-1):
    for j in range (1,i+1):
        print("*", end=" ")
    print()
