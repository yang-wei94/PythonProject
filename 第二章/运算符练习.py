# # 案例1: 计算输入的三个整数的平均数
# x = float(input("请输入x:"))
# y = float(input("请输入y:"))
# z = float(input("请输入z:"))
#
# avg_data = (x + y + z) / 3
# print(f"{x},{y},{z}这三个数的平均数为:{avg_data}")
#
# # 案例 2: 要求输入梯形的上底、下底、高,然后计算梯形面积
# top = float(input("请输入梯形的上底: "))
# bottom = float(input("请输入梯形的下底: "))
# height = float(input("请输入梯形的高: "))
#
# print(f"梯形的面积是: {(top + bottom) * height / 2}")
#
# # 要求输入圆的半径，然后计算圆的周长和面积 (周长: 2πr，面积：πr²)
# r = float(input("请输入圆的半径:"))
#
# print(f"圆的周长: {2 * 3.14 * r}")
# print(f"圆的面积: {3.14 * r ** 2}")

#  案例4：身体质量指数BMI的计算（BMI = 体重(kg) / 身高(m)²）
#  1. 输入体重(单位kg)
#  2. 输入身高(单位m)
#  3. 计算身体质量指数BMI并输出

weight = float(input("请输入体重(单位kg):"))
height = float(input("请输入身高(单位m):"))

print(f"身体质量指数BMI: {weight / (height ** 2)}")

