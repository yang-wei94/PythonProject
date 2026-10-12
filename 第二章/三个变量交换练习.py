#现有三个变量,分别为: a = 100, b = 200, c = 300,现需要将这三个变量值进行交换,将a,b,c的值分别赋值给c,a,b,并将其输出到控制台.
#这是我自己做的
a = 100
b = 200
c = 300

d = a # d = 100
a = b # a = 200
b = c # b = 300
c = d # c = 100
print(a, b, c)

#这是练习答案
a = 100
b = 200
c = 300

temp = a
a = b
b = c
c = temp

print(a)
print(b)
print(c)