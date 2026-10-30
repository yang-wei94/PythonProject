#------------------------------------函数 -  变量的作用域-----------------------------
# 全局变量
num = 100

# 定义函数
def circle_area(r):
    # 局部变量 : 只能在函数内部使用
    pi = 3.14
    area = pi * r * r

    global num
    num = 10000

    print("num =", num) # 10000

    return area


# print("pi =", pi)
# print("area =", area)
# print("r =", r)
#调用函数
c_area= circle_area(10)
print(c_area)

print("num =", num) # 10000


# -------------------------------------- 函数 - 传参方式 ------------------------------------
# 定义函数
def reg_stu(name, age, gender, city):
    print(f"注册成功,姓名:{name}, 年龄:{age}, 性别:{gender}, 城市:{city}")
    return {"name":name, "age":age, "gender":gender, "city":city}

# 传参方式一:  位置参数
stu = reg_stu("张三",18,"男", "北京")
print(stu)


# 传参方式二: 关键字参数
stu = reg_stu(name="王林", age=28, gender="男", city="北京")
print(stu)

stu = reg_stu(gender="女", city="长沙", name="李慕婉", age=19)
print(stu)

# 传参方式三:  位置参数 + 关键字参数------>  位置参数在前,关键字参数在后
stu = reg_stu("王麻子",15, city="上海", gender="男")
print(stu)


# ------------------------------- 函数 - 默认参数 -------------------------
# 定义函数
def reg_stu(name, age, gender="男", city="北京"):
    print(f"注册成功,姓名:{name}, 年龄:{age}, 性别:{gender}, 城市:{city}")
    return {"name":name, "age":age, "gender":gender, "city":city}

# 调用函数
stu = reg_stu("王林", 20)
print(stu)

stu = reg_stu("李慕婉", 20, "女")
print(stu)

stu = reg_stu("韩立", 18, city="上海")
print(stu)


# -------------------------------- 函数 - 不定长参数(位置参数 *args ---->元组)-------------------------------
#  需求: 根据传入的这批数据,计算这批数据的最小值,最大值,平均值
def calc_data(*args):
    min_data= min(args)
    max_data = max(args)
    avg_data= sum(args)/len(args)
    return min_data,max_data,round(avg_data,1)

# 调用函数
print(calc_data(2, 6, 7, 9, 12, 50, 63))
print(calc_data(2, 6, 7, 9, 12, 50, 63, 98, 105, 120, 180))


# -------------------------------- 函数 - 不定长参数(关键字参数 **kwargs ---->字典)-------------------------------
#  需求: 根据传入的这批数据,计算这批数据的最小值,最大值,平均值
def calc_data(*args,**kwargs):
    min_data= min(args)
    max_data = max(args)
    avg_data= sum(args)/len(args)
    if kwargs.get("round") is not None:
        avg_data = round(avg_data,kwargs.get("round"))
    if kwargs.get("print"):
        print(f"最大值是:{max_data},最小值是:{min_data},平均值是:{avg_data}")
    return min_data,max_data,avg_data

# 调用函数

print(calc_data(2, 6, 7, 9, 12, 50, 63, 98, 105, 120, 180))
print(calc_data(2, 6, 7, 9, 12, 50, 63, round=3,print=True))


