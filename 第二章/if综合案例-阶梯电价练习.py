#居民年度用电电费计算: 根据输入的用电度数,计算出电费
#   电费采用阶梯式计价方式,按照用户的消费的电量分段定价,用电价格随用电量增加呈阶梯式逐级递增的一种电价定价机制
#  阶梯电价规则:
#           第一档:2880度以下,电费单价0.4883元/度
#           第二档:2880-4800度,电费单价0.5383元/度
#           第三档:4800度以上,电费单价0.7883元/度

##   我写的
num = float(input("请输入您的总用电数:"))
if num >= 2880:
    if num >= 2880 and num <= 4800:
        print(f"您的年度电费应是:", (num-2880) * 0.5383 + 2880 * 0.4883)
    else:
        print(f"您的年度电费应是:" , (num - 4800) * 0.7883 + (4800 - 2880) * 0.5383 + 2880 * 0.4883)
else:
    print(f"您的年度电费应是:",  num * 0.4883)






#############################    案例答案      ###########################
usage_elec = int(input("请输入用电度数: "))

# 定义阶梯电价
first_max = 2880  # 第一档上限
second_max = 4800  # 第二档上限

first_price = 0.4883  # 第一档单价
second_price = 0.5383  # 第二档单价
third_price = 0.7883  # 第三档单价

total_cost = 0.0  # 总电费

# 使用if语句进行阶梯电价计算
if usage_elec <= first_max:
    # 全部在第一档
    total_cost = usage_elec * first_price
elif usage_elec <= second_max:
    # 第一档部分
    first_cost = first_max * first_price

    # 第二档部分
    second_usage = usage_elec - first_max
    second_tier_cost = second_usage * second_price
    total_cost = first_cost + second_tier_cost
else:
    # 第一档部分
    first_cost = first_max * first_price

    # 第二档部分
    second_usage = second_max - first_max
    second_cost = second_usage * second_price

    # 第三档部分
    third_usage = usage_elec - second_max
    third_cost = third_usage * third_price
    total_cost = first_cost + second_cost + third_cost

print(f"{usage_elec} 度的电费是: {total_cost} 元")