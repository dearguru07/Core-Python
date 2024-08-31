
# print('Hello to all')
# def Guru():
#     print('hello to all my friends')
# Guru()    
# print('hello namaste') 

   
# OOPS ---------------


# class Guru():
#     def __init__(self):   #--------------constractor
#         print('it is method...')
#     print('Hello to every one')    
#     def gurucharan(self):
#         print('guru is here')
#     def new(self):
#         print('new method it is...')

# res=Guru()
# res.gurucharan()
# res.new()

# classes containes methods and constactors(__init__)-----    
# constrzcotr direcly excetucte when ever u creates create object    
# constructor by deafalt it will take self as parameter

# def Fun():
#     print('Heloo')
#     a=20
#     return a
# x=Fun()
# print(x)


# class itself():
#     def __init__(self):
#        self.a=20
#         # print(a)
# x=itself()        
# print(x.a)

# inside the functns use return statement for returning the value outside of the functns
# in class componets use the self as a para for the rreturing the outside of the class componrt


# file handling using functional componets------------


# def File():
#     data="in class componets use the self as a para for the rreturing the outside of the class componrt"
#     with open('guru.text','w') as file:
#         print('data stred printing')
#         file.write(data)
#         print('data is printed successfully')
# File()


# def newFile(name,number):
#     with open('names.txt','a') as file:
#         print('data is printing')
#         file.write(name+'\n')
#         print('data is printed ucessfully')
#     with open('numbers.txt','a') as file:
#         print('data is printing')
#         file.write(number+'\n')
#         print('data is printed ucessfully') 
# x=str(input('enter ur name'))           
# y=str(input('enter ur mbl nunber'))           
# newFile(x,y)        


# file handling using class componets----------


# class file():
#     def __init__(self,x,y):
#         self.name=x
#         self.number=y
#         with open('names.txt','a') as file:
#             print('data is peinting')
#             file.write(self.name+'\n')
#             print('data is printed')
#         with open('numbers.txt','a') as file:
#             print('data is peinting')
#             file.write(self.number+'\n')   
#             print('data is printed')
# x=str(input('enter name'))            
# y=str(input('enter number'))            
# ref=file(x,y)             


# inheritence----------------------------

# single inheritence----------

# class Father():
#     def land(self):
#         print('dad have land')
#     def house(self):
#         print('dad have house also')    
# F=Father()

# class Guru(Father):
#     def nothing(self):
#         print("i don't have any thing")
# C=Guru()
# C.nothing()  
# C.house()      


# mutli level inheritence---------------

class GFather():
    def Land(self):
        print('Gf have land')
    def HOuse(self):
        print('gf have house')    
G=GFather()        
class Father(GFather):
    def Money(self):
        print('father have money')
    def Job(self):
        print('father have job')   
F=Father()   
class Me(Father):
    def nothing(self):
        print('i dont have any thing')        
M=Me()      
M.nothing()
M.Land()
M.HOuse()
M.Job()


# mutliple  inheritence---------------


class Father():
    def Land(self):
        print('father have land')
    def job(self):
        print('father have job')    
f=Father()
class Mother():
    def money(self):
        print('mother have money')
    def Food(self):
        print('mother have food also')    
m=Mother()
class Guru(Father,Mother):
    def nothing(self):
        print('i dont have anything')        
g=Guru()        
g.nothing()
g.Food()
g.job()
g.money()
g.Land()