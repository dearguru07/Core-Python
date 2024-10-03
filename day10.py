# encapsulation------------------

# class Guru():
#     def __init__(self):
#         self.a=10
#         self.b=32
#         print(self.a+self.b)
# Guru()        
# class Charan():
#     def add(Guru):
#         print(self.a+self.b)
# res=Charan()
# res.add(10,54)        

# public varibles---------

# class Guru():
#     def __init__(self,x,y):
#         self.a=x
#         self.b=y
#     def Add():
#         print(self.a+self.b)    
# res=Guru(10,5)  
# print(res.a) 
# print(res.b) 


# private varibles-----------------

# class Guru():
#     def __init__(self,x,y):
#         self.__a=x
#         self.__b=y
#     def Add():
#         print(self.__a+self.__b)    
# res=Guru(10,47)        
# print(res.a)
# print(res.b)

# public varibles-------------------

# class Accounnt():
#     def __init__(self,x):
#         self.a=x
#         print('money debited from account',self.a)
#     def Guru(self):
#             print('money is creadite to guru',self.a)
# res=Accounnt(5000)
# res.a=1000
# res.Guru()            


# private varibles-----------------

# class Accounnt():
#     def __init__(self,x):
#         self.__a=x
#         print('money debited from account',self.__a)
#     def Guru(self):
#             print('money is creadite to guru',self.__a)
# res=Accounnt(5000)
# res.a=1000
# res.Guru()            


# class Accounnt():
#     def __init__(self,x):
#         self.a=x
#         # self.b=y
#         print('money is debited',self.a)
#     def debited(self):
#         print('money is credited',self.a)
# res=Accounnt(400)    
# res.a=100    
# res.debited()


import qrcode as qr

start=str(input('From:'))
end=str(input('To:'))
Tkts=int(input('How many Tkts:'))
data=start+"\n"+end+"\n"+str(Tkts)
# print(data)
image=qr.make(data)
image.save('qrcode.png')
print('qr code is generated... Happy Jounery')

