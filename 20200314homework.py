# Python练习题：
# 1、打印小猫爱吃鱼，小猫要喝水
# class Animal(object):
#     name = 'cat'
#     def eat(self,food):
#         print("%s爱吃%s"%(self.name,food))
#
#     def drink(self):
#         print("%s要喝水"%(self.name))
#
# a =Animal()
# a.name = '小猫'
# a.eat('鱼')
# a.drink()

# 2、小明爱跑步，爱吃东西。
# 1）小明体重75.0公斤
# 2）每次跑步会减肥0.5公斤
# 3）每次吃东西体重会增加1公斤
# 4）小美的体重是45.0公斤
# class Person(object):
#     def __init__(self,name,weight):
#         self.name = name
#         self.weight = float(weight)
#     def run(self,n):
#         for i in range(1,n+1):
#             self.weight -= 0.5
#         print('%s跑步%d次，体重是%s'%(self.name,i,self.weight))
#     def eat(self,m):
#         for j in range(1,n+1):
#             self.weight += 1
#         print('%s吃东西%d次，体重是%s'%(self.name,j,self.weight))
#
#
# n = int(input('请输入跑步次数:'))
# m = int(input('请输入吃东西次数：'))
# a = Person('小明','75')
# a.run(n)
# a.eat(m)


# 3、摆放家具
# 需求：
# 1）.房子有户型，总面积和家具名称列表
#    新房子没有任何的家具
# 2）.家具有名字和占地面积，其中
#    床：占4平米
#    衣柜：占2平面
#    餐桌：占1.5平米
# 3）.将以上三件家具添加到房子中
# 4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
# class House(object):
#
#     def __init__(self,huxing,area):
#
#         self.huxing = huxing
#         self.area = float(area)
#         self.jiajulist = []
#
#
#
#     def Addjiaju(self,jiaju):
#
#         self.jiajulist.append(jiaju)
#         if jiaju == '床':
#             self.area -= 4
#         elif jiaju == '衣柜':
#             self.area -= 2
#         else:
#             self.area -= 1.5
#         print(self.huxing,self.area,self.jiajulist)
#
#
# a =House('两居一卫',90)
# listj = ['床','衣柜','餐桌']
# for i in listj :
#     a.Addjiaju(i)


#
# 4.士兵开枪
# 需求：
# 1）.士兵瑞恩有一把AK47
# 2）.士兵可以开火(士兵开火扣动的是扳机)
# 3）.枪 能够 发射子弹(把子弹发射出去)
# 4）.枪 能够 装填子弹 --增加子弹的数量



