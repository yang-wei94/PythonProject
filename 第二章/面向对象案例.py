"""
案例:
      采用面向对象的变成思想,开发一个购物车管理系统,实现商品信息的添加,修改,删除,查询功能.系统使用自定义对象存储商品数据,通过控制台菜单与用户交互.
      具体功能如下:
          1. 添加购物车: 用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车
          2. 修改购物车： 要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息
          3. 删除购物车： 要求用户输入要删除的购物车商品名称，根据名称删除购车中的商品
          4. 查询购物车： 将购物车中的商品信息展示出来，格式为：“商品名称：xxx， 商品价格：xxx， 商品数量： xxx”
          5. 退出购物车
"""
class Goods:
    def __init__(self, name, price, number):
        self.name = name
        self.price = price
        self.number = number

    def __str__(self):
        return f"商品名称:{self.name}, 商品价格:{self.price}, 商品数量:{self.number}"

    def update_information(self, price=None, number=None): # 修改商品信息
        if self.price is not None:
            self.price = price
        if self.number is not None:
            self.number = number

class ShoppingCart(Goods):
    systeam_version = "1.0.0"
    systeam_name = "购物车管理系统"

    def __init__(self):
        self.goods_cart = []

    # 添加购物车
    def add_goods(self):
        name = input("请输入要添加的商品信息:")
        for s in self.goods_cart:
            if s.name == name:
                print("该商品已存在,请重新输入!")
                return

        price = int(input("请输入要添加商品的价格:"))
        number = int(input("请输入要添加商品的数量:"))

        good = Goods(name, price, number)
        self.goods_cart.append(good)
        print("商品添加成功!")

    # 修改购物车
    def update_goods(self):
        name = input("请输入要修改的商品:")
        for s in self.goods_cart:
            if s.name == name:
                print(f"该商品的信息为:{s}")

                price = int(input("请输入要修改商品的价格:"))
                number = int(input("请输入要修改商品的数量:"))
                s.update_information(price, number)
                print(f"该商品信息修改成功,修改后为:{s}")
                return
        print("未找到该商品,修改失败!!")

    # 删除购物车
    def delete_goods(self):
        name = input("请输入要删除的商品:")
        for s in self.goods_cart:
            if s.name == name:
                self.goods_cart.remove(s)
                print("该商品删除成功!")
                return
        print("未找到该商品,删除失败!")

    # 查询商品信息
    def query_goods(self):
        name = input("请输入要查询的商品信息:")
        for s in self.goods_cart:
            if s.name == name:
                print(f"查询的商品信息为:{s}")
                return
        print("未找到该商品,查询失败!")

    # 遍历所有商品信息
    def list_goods(self):
        for s in self.goods_cart:
            print(s)

    # 运行系统
    def run(self):
        print(f"欢迎使用{ShoppingCart.systeam_name} V{ShoppingCart.systeam_version}")

        while True:
            print("##################")
            print("#  1.添加购物车    #")
            print("#  2.修改购物车    #")
            print("#  3.删除购物车    #")
            print("#  4.查询指定商品  #")
            print("#  5.遍历所有商品  #")
            print("#  6.退出系统     #")
            print("##################")
            print()

            choice = input("请输入你的操作指令(1-6):")
            match choice:
                case "1": # 添加购物车
                    self.add_goods()
                case "2": # 修改购物车
                    self.update_goods()
                case "3": # 删除购物车
                    self.delete_goods()
                case "4": # 查询购物车
                    self.query_goods()
                case "5": # 遍历购物车
                    self.list_goods()
                case "6": # 退出系统
                    print("Bye~~")
                    break
                case _:
                    print("无效指令,请重新输入!")

if __name__ == '__main__':
    shopping_cart = ShoppingCart()
    shopping_cart.run()