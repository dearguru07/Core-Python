# dynamic inputs-----------------------


# x=10
# print(x)

# x=int(input('Enter a number'))
# x=float(input('enter a nuynber'))
# print(x)

# x=int(input('Enter a number'))
# y=int(input('Enter new a number'))
# print(x+y)


# Trnary operators=---------------------------


# age=22
# x="voter valid" if age>18 else "not valid"
# print(x)


# number=0
# x='English' if number==1 else 'tamil' if number==2 else 'hindi' if number==3 else 'malayalm' if number==4 else 'urdu'

# print(x)



# if conditions----------------------

# age=18
# if age>18:
#     print('valid')
# else:
#     print('not valid')    


# age=18
# if True:
#     print('valid')
# else:
#     print('not valid')    


# brand="sprit"
# if brand=='thumsup':
#     print('mahesh mabu hero')
# elif brand=='mountdow':
#     print('akhil hero')    
# elif brand =='sprit':
#     print('nani hero')    
# else:
#     print('vd hero')  


# brand=str(input('enter a brand name:'))
# if brand=='thumsup':
#     print('mahesh mabu hero')
# elif brand=='mountdow':
#     print('akhil hero')    
# elif brand =='sprit':
#     print('nani hero')    
# else:
#     print('vd hero')    


# number=int(input("enter a number"))
# if number ==1:
#     print('Telugu')
# elif number==2:
#     print('Hindi')    
# elif number==3:
#     print('Kannada')    
# elif number==4:
#     print('English')    
# elif number ==5:
#     print('Tamil')    
# elif number ==6 :
#     print('Malayalam')       
# else:
#     print('no languge')



# Looooops  (for loop)----------------------------------

# if u know the itarations advancely , we choose for loop---------

# n=10
# for i in range(n,0,-1):
#     print(i)


# if u don't know the itarations advancely , we choose for loop---------


# x=1
# while x<=1000:
#     print(x)
#     x=x+1

# a="Hello to all my dear friends"
# for x in a:
#     print(x)


# scale=72
# while scale>20:
#     print('thusnamli')
#     break
# else:
#     print("no sunammi")    


# while True:
#     print("Infinate loop")
#     break


# while False:
#     print("Infinate loop")
#     break
# else:
#     print('this was the else part in while loop')


# control flow satatements-------------------------------


# pass --ingrone the error;
# break  --terminate
# continue --skip


# for i in range(50):
#     print(i)
#     if i==29:
#         break



# for i in range(100):
#     if i%2==0:
#         print(i)


# if True:
#     print('If part will excetucte')
#     pass
# else:
#     print('Else part will excute')


# -----------removing the indandetion error----------- [Using of pass]

# if True:
#     pass   

# -----------------stoping the for loop-----------

# for i in "gurucharan":
#     if i=="c":
#         break
#     print(i)
# there are u is the last letter, so that C and remaing values are not print


# -----------skipping the one letter--------------


for i in "gurucharan":
    if i=="c":
        continue
    print(i)
    
# there are c will remove and remainig values are printing
    
