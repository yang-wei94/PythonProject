#这是我第一次的Python实战练习
print("############")
print("# 白日依山尽 #")
print("# 黄河入海流 #")
print("# 欲穷千里目 #")
print("# 更上一层楼 #")
print("############")


num_list = []

for i in range(10):
    number = int(input("请输入数字:"))
    num_list.append(number)
print(num_list)

num_list.sort()
print(num_list)

print("最小值:", num_list[0])
print("最大值:", num_list[-1])
print("平均值:", sum(num_list)/len(num_list))