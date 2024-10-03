# functions----------------------------

# def grind():
#     print('Hello world')
# grind()    


# def grind(a,b,c,d):
#     print('juice with this fruits',a,b,c,d)
# grind('banana','apple','sugar','milk')    


# positional argments------------------

# def Code(a,b):
#     print(a+b)
# Code(4,8)    

# keyword argments------------------

# def Add(a,b):
#     print(a-b)
# Add(a=12,b=2)    


# varible length argments---------------------

# def Show(*x):
#     print(x)
#     print(type(x))
# Show(10,20,8,7,32,45)    


# print() function calling--------------

# asnamas function-----------


# def manger(x):
#     print(x*x)
# manger(25)


# s=lambda x:x*x
# print(s(5))

# guru=lambda a:a*a
# print(guru(4))


# from pywhatkit import *

# phone="+919346860132"
# msg='Hello Guru'
# hour=14
# mint=15
# pywhatkit.sendwhatmsg(phone,msg,hour,mint)


# from random2 import *

# x=randint(000000,999999)
# print(x)



import pywhatkit
from random2 import *

phone_number='+918688174622'
otp=randint(000000,999999)
z=str(otp)
msg='OTP is'+z +'pls dont share any one'
hour=15
mints=12
pywhatkit.sendwhatmsg(phone_number,msg,hour,mints)
