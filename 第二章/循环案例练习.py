#  用户名密码登录练习  :  正确的用户名和密码为: admin/666888, zhangsan/123456, taoge/888666
#                    5次登录机会,输入错误5次,不允许再操作了

for i in range(5):
    username = input("请输入正确的用户名:")
    password = input("请输入正确的密码:")
    if username == "admin" and password == "666888":
        print("登陆成功.")
        break
    elif username == "zhangsan" and password == "123456":
        print("登录成功.")
        break
    elif username == "taoge" and password == "888666":
        print("登陆成功.")
        break
    else:
        print("登录失败,请重新登录.")
        if i== 4:
            print("登陆失败超过5次,不允许再登录")
            break