# # 案例
# # 1. 定义一个函数: 根据输入的底和高计算三角形面积的函数(三角形面积 = 底 * 高 / 2)
# def triangle_area(d,h):
#     """
#     根据输入的底和高,计算三角形的面积
#     :param d: 底
#     :param h: 高
#     :return: 三角形面积
#     """
#     area = d * h / 2
#     return area
#
# d = float(input("请输入三角形的底:"))
# h = float(input("请输入三角形的高:"))
#
# tri_area = triangle_area(d,h)
# print(f"三角形的面积为:{tri_area}")
#
# # 案例 2: 定义一个函数:计算传入的字符串中元音字母的个数(元音字母为 aeiouAEIOU)
# def count_aeiou(s): # helloworld
#     """
#     统计字符串中元音字母的个数
#     :param s: s 字符串
#     :return: 元音字母的个数
#     """
#     num = 0
#     for w in s:
#         if w in "aeiouAEIOU":
#             num += 1
#     return num
#
# print(count_aeiou("hello python hello world ok"))



# # 案例3: 定义一个函数: 计算传入的班级学员高考成绩列表中成绩的最高分,最低分,平均分(保留1位小数),并返回
# def calc_score(score_list):
#     """
#     计算传入的班级学员高考成绩列表中成绩的最高分,最低分,平均分
#     :param score_list: 分数列表
#     :return: 最高分,最低分,平均分
#     """
#     max_s = max(score_list)
#     min_s = min(score_list)
#     avg_s = round(sum(score_list) / len(score_list),1)
#     return max_s, min_s, avg_s
#
# s_list= [560, 680, 590, 620, 608, 672, 560, 630, 645, 485, 500]
# max_score,min_score,avg_score = calc_score(s_list)
# print("最高分:", max_score)
# print("最低分:", min_score)
# print("平均分:", avg_score)
#
# #----------------------练习----------------------------------------
# # 练习 1:
# """1. 定义一个函数: 根据传入的分数,计算对应的分数等级并返回
#       分数 >= 90: A
#       分数 >= 75: B
#       分数 >= 60: C
#       分数 < 60: D
# """
# def calc_rank(s):
#     if s >= 90:
#         return "A"
#     elif s >= 75:
#         return "B"
#     elif s >= 60:
#         return "C"
#     else:
#         return "D"
# s = float(input("请输入您的分数:"))
# rank = calc_rank(s)
# print("您的等级为:",rank)
#

# 练习 2 :
"""
2. 定义一个函数,用于判断一个字符串是否为回文串,返回Bool值
   ``把字符串反转,如果和原字符串相同,就是回文串. (如: "level", "radar", "黄山落叶松叶落黄山") 
# """
# def judge_str(str):
#     if str == str[::-1]:
#         return True
#     else:
#         return False
#
# str = "上海自来水来自海上"
# print(judge_str(str))


#  试题里的答案
# 定义一个函数，用于判断一个字符串是否是回文串，返回bool值。
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("level"))
print(is_palindrome("hello"))
print(is_palindrome("黄山落叶松叶落山黄"))
print(is_palindrome("12321"))
print(is_palindrome("12345"))


# # 3. 定义一个函数,完成时间转换功能,将传入的秒,转化为小时、分钟、秒
# def convert_time(t):
#     hour = round(t / 3600, 2)
#     minute = round(t / 60, 1)
#     return hour, minute
#
# print(convert_time(360000))
# print(convert_time(600))
# print(convert_time(1200))
# print(convert_time(700))
# print(convert_time(75))


# 定义一个函数：完成时间转换功能，将传入的秒转换为小时、分钟、秒。
def time_convert(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    second = (seconds % 3600) % 60
    return f"{seconds}秒 转换为 {hours} 小时 {minutes} 分钟 {second} 秒"

print(time_convert(3772))




# 4.定义一个函数,根据传入的三角形的三个边的边长,判定三角形的类型(等边,等腰,普通,或者不能构成三角形)
def triangle_convert(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "等边三角形"
        elif a == b or a == c or b == c:
            return "等腰三角形"
        else:
            return "普通三角形"
    else:
        return "不能构成三角形"


print(triangle_convert(3,4,5))
print(triangle_convert(3,3,5))
print(triangle_convert(3,3,5))
print(triangle_convert(3,3,3))
print(triangle_convert(3,5,5))
print(triangle_convert(3,4,7))
print(triangle_convert(8,8,8))
