# -------------------------字符串常用方法------------------
from 第二章.list案例 import str_list

s = "Hello-python-Hello-world"

# find()  查找指定字符串第一次出现的索引位置
index = s.index("-")
print(index)

# count() 统计子字符串在指定字符串中出现的次数
c = s.count("o")
print(c)

# upper()  转为大写
su = s.upper()
print(su)

# lower()  转为小写
sl = s.lower()
print(sl)

# spilt() 将字符串按照指定字符串切割---列表
slist = s.split("-")
print(slist)

# strip() 去除字符串两端的空格
ss = s.strip()
print(ss)

# replace()将字符串中的指定子串替换为新的内容
sr = s.replace("-", "_")
print(sr)

# startswith() / endswith() 预判字符串是否是以指定的字符串开头 / 结尾, 返回布尔值
print(sr.startswith("Hello"))
print(sr.endswith("python"))


##----------------------------  字符串案例------------------
# 案例1: 邮箱格式验证: 用户输入一个邮箱,验证邮箱格式是否正确(包含一个@ 和至少一个. ), 如果输入正确,输出"邮箱格式正确",否则输出"邮箱格式错误"

# 1. 接收用户输入的邮箱
mail = input("请输入邮箱:")

# 2. 判断邮箱的格式
if mail.count("@") == 1 and mail.count(".") >=1:
    print(f"{mail}是合法的邮箱")
else:
    print(f"{mail}是非法的邮箱")





# 1. 输入一个字符串, 判断该字符串是否是回文(两边对称) 。  "黄山落叶松叶落山黄"  "上海自来水来自海上"
s = input("请输入一个字符串: ")

# 方式一(双指针法): 思路是从两边向中间遍历, 基于索引获取两边字符对比, 如果两边的字符不相等, 则不是回文, 否则是回文。
left = 0 # 左索引
right = len(s) - 1 # 右索引
flag = True

while left < right:
    if s[left] != s[right]:
        flag = False
        break
    left += 1
    right -= 1

if flag:
    print(f"'{s}' 是回文")
else:
    print(f"'{s}' 不是回文")


# 方式二:
if s == s[::-1]:
    print(f"'{s}' 是回文")
else:
    print(f"'{s}' 不是回文")



# 将用户输入的10个字符串,反转后全部转化为大写,然后记录在列表中,最后将列表内容,遍历输出出来
s_list = []

for i in range(10):
    s = input("请输入一个字符串:")
    s_list.append(s[::-1].upper())
print("输入的字符串为:", s_list)

print("--------------------")
for s in s_list:
    print(s)


