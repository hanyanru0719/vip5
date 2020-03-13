# 一、python语言学习（上）
# 练习：分别定义一个集合和一个字典
#a = set() #定义一个集合
#b = {} #定义一个字典


# 1-   为集合和字典分别插入元素：55（d：55）
#a.add(55)
#print(a)
#b['d'] = 55
#print(b)


# 2-   分别删除集合和字典内的一个元素
# aset = {1,2,3,4,5}
# adic ={'a':4,'b':5,'c':6}
# aset.remove(2)
# del adic['a']
# print(aset,adic)


# 3-   取出字典内的所有值（value）和集合组合一个列表
# aset = {1,2,3,4}
# adic = {'a':4,'b':5,'c':6,'d':7}
# a = list(adic.values())
# a.extend(list(aset))
# print(a)


# 4-集合和字典的区别
#   ①创建空集合：set() 创建空字典 {}
#   ②集合不可重复，无序 字典键不可重复，无序

# 二、python语言学习（下）

# 练习：计算1+2+3+4……+100的和

# i = 1
# s = 0
# while i <= 100:
#     s += i
#     i += 1
# print(s)

# 1、求10的阶乘

# p = 1
#
# for i in range(1,11):
#     p = p*i
# print(p)


# 2、求100以内能被3整除的数，并将作为列表输出

# th = []
#
# for i in range(1,101):
#     if i % 3 == 0 :
#         th.append(i)
# print(th)



# 3、列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表

# ogrl = [1,2,3,4,3,4,2,5,5,8,9,7]
# newl =[]
# for i in ogrl:
#     if i not in newl:
#         newl.append(i)
# print(newl)


# 4、求斐波那契数列 1  1  2  3  5  8  13
# def feibo(n):
#     a = 1
#     b = 1
#     i = 0
#     d = []
#     while i <= n:
#         if i == 0:
#             d.append(a)
#             i = i + 1
#         else:
#             c = a
#             a = b
#             b = c + a
#             i = i + 1
#             d.append(a)
#     print(d)
#
# feibo(1000)


# 5、找出1-100里面的质数

# for i in range(1,101):
#     A = []
#     for j in range(1,i):
#         if i > 1:
#             a = i%j
#             if a==0:
#                 A.append(i)
#     if len(A) == 1:
#         print(A[0])


# 6、读取以下文件：a-全部内容；b-每一行的内容；c-读取所有行的内容

# f = open(r'/Users/hanyanru/Desktop/pyyhon_study/liangwav/test.txt','r')
# # print(f.read()) #读取文件全部内容
# # print('~~~~')
# # f.seek(0)
# # for i in f.readlines():
# #     print(i.strip('\n')) #读取文件每一行的内容
# # print('~~~~~')
# # f.seek(0)
# # s = []
# # for j in f.readlines():
# #     s.append(j.strip('\n'))
# # print(s) #读取文件所有行的内容
#f.close()



# 7、读取以下文件的全部内容，并将所有的数字去重后，放入一个列表

# f = open(r'/Users/hanyanru/Desktop/pyyhon_study/liangwav/7ti.txt','r')
# print(f.read())#读取文件的全部内容
# print('....................')
# f.seek(0)
# ali = []
# for i in f.readlines():
#     j =i.strip('\n').split('，')
#     print(j)
#     for x in j:
#         y =int(x)
#         #print(y)
#         if y not in ali:
#             ali.append(y)
# print(ali)
#
# f.close()


# 8、将以上文件的全部内容写入一个新的文件，并按照从小到大的顺序
# with open(r'/Users/hanyanru/Desktop/pyyhon_study/liangwav/7ti.txt','r') as f :
#     ali = []
#     bli = []
#     with open(r'/Users/hanyanru/Desktop/pyyhon_study/liangwav/8ti.txt','w+') as nf:
#         for i in f.readlines():
#             j = i.strip('\n').split('，')
#             for x in j:
#                 y = int(x)
#                 ali.append(y)
#         ali.sort()
#         #print(ali)
#         for m in ali:
#             n = str(m)
#             bli.append(n)
#             bli.append('，')
#
#         nf.writelines(bli)


# 9、读取data文件中的数据，将所有的数字去重并按照从小到大的顺序写入backup文件

# with open(r'/Users/hanyanru/Desktop/pyyhon_study/liangwav/7ti.txt','r') as f :
#      ali = []
#      bli = []
#      with open(r'/Users/hanyanru/Desktop/pyyhon_study/liangwav/backup.txt','w+') as nf:
#          for i in f.readlines():
#              j = i.strip('\n').split('，')
#              for x in j:
#                  y = int(x)
#                  if y not in ali:
#                     ali.append(y)
#          ali.sort()
#          print(ali)
#          for m in ali:
#              n = str(m)
#              bli.append(n)
#              bli.append('，')
#
#          nf.writelines(bli)




    

     




























