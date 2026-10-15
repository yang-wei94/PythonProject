# while循环: 打印10遍"人生苦短,我用python"

i = 0
while i < 10:
    print("人生苦短,我用python")
    i += 1
else:
    print("循环结束.")

#  while案例:  计算1-100之间所有偶数的累加之和
total = 0 #记录累加之和

i = 1  # 循环开始的数

while i <= 100:
    if i % 2 == 0:
        total += i
    i += 1

print(f"1-100之间的偶数相加之和:{total}")
