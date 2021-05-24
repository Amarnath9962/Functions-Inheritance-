# Hi friends here i practiced some more topics in the functions
# # # 1.Example
# def Fun_1():
#     print("Hi Frineds this is Amarnath from chennai .\nSeeking the jon in the softwate domain..")
# Fun_1()
# def Fun_2(name,age):
#     print("Hi this is "+name+'. My age is ',age)
#     x = age
# Data = Fun_2('Amarnath',28)
# print(Data)

# 2.Example (Here i'm practing the with class modules
# class First:
#     x = 12*28
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def PrintName(acb):
#         print(acb.name)
# F = First("Amarnath",26)
# print(F.x)
# F.PrintName()
#
# class Fruits:
#     def __init__(self,*FruitNames):
#         self.FruitName = FruitNames
#
#     def Name(self,*Prices):
#         self.Prices = Prices
#         for x in self.FruitName:
#             for y in self.Prices:
#                 print(x,y)
#                 continue
# F = Fruits('Apple','Grapes','Mango')
# F.Name(12,25,36)

# class Fruits :
#     def __init__(self,*items):
#         self.items = items
#     def Fuits_Names(self,*price):
#         self.price = price
#         for x in range(len(self.items)):
#             print("The "+self.items[x]+" price is : Rs = "+str(self.price[x])+"/-")
# F = Fruits('Apple','Grapes','Lemon')
# F.Fuits_Names(12,15,26)

# # inheretence  in python and encapsulatins in functions
# class Animals:
#     "Hi this is Animal class having a some text in the animala class "
#     __Name ='Amarnath K'
#     __password = '123'
#
#     def __init__(self,Name,age):
#         self.Name = Name
#         self.age = age
# class Personal_Details(Animals):
#     "Hi this is checking docstring.\nMy name is amarnath k from chennai seeking the job in the Data science roles. "
#     __username = "amar080392gmail.com"
#     __password = 'Amar1552@..'
#     def __init__(self,Name,age,Salary,Phone):
#         self.Salary = Salary
#         self.Phone = Phone
#         self.__username = "amar080392gmail.com"
#         self.__password = 'Amar1552@..'
#         super().__init__(Name,age)
#     def Person_Information(self):
#         print("The Name of the person is",self.Name)
#         print("The Person age is :",self.age)
#         print("The Person salary is Rs = "+str(self.Salary)+"/-")
#         print("The Person having a Phone Type :",self.Phone)
#         print("Username is ",self.__username)
#         print("Password is ",self.__password)
# F= Personal_Details('Amarnath',28,21000,9962720335)
# F.Person_Information()
# # A = Animals()
# print(F.__doc__)
# print(isinstance(F,Animals))
# print(F._Personal_Details__username)
# print(F._Animals__Name,F._Animals__password)

