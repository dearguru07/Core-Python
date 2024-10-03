# print('Hello world......')

# numbers=1254
# print(type(numbers))

# x=1.25
# print(type(x))


# intreprester --> it will take prgrm lngueg as input and converts into assembler languge--------


# day------------2

# boolean-------------------

# x=True+True
# print(x)

# x=False+True
# print(x)


# x,y,z=10,'guru',22
# print(y)
# print(type(y))

# bytes----------------

# x=100
# y=100
# print(id(x))
# print(id(y))

# x=[1,2,3,15]
# y=bytes(x)
# print(y)
# print(type(y))


# x=[1,2,3,15,255]   #we csn't give gratterthn 255 and it will allow only numbers
# y=bytes(x)
# for i in x:print(i)

# y[3]=200  #bytes are immutables

# print(y[2])
# print(type(y))


# bytearray--------------------

# x=[1,2,3,5,8,255]
# y=bytearray(x)
# y[4]=244    #it's muttable   
# print(y[4])
# y.remove(255)
# print(y)
# print(type(y))


#tuples------------------------

# x=(1,25,45,'hello')
# print(x[2])
# print(x)
# print(type(x))
# it is also immutables---------


# dict-------------------------


x={1:"guru",2:"charan",3:"python",8:21,7:'Heloo'}
print(x[1])
print(x)
print(type(x))


# a=[{1:"guru",2:"charan",3:"python",8:21,7:'Heloo'},{1:"raju",2:"venky",3:"javascript",8:20,7:'Helollo'}]
# a.append(4)
# print(a)
# print(type(a))


# set--------------------

# d={100,200,48,35,77,500,'guru'}
# print(d[0])!!!!
# d.add(24)
# d.remove(100)
# print(d)
# print(type(d))
# it is also mutables and it does not follow indexing---------


# list---------------------/-

# list=[100,200,500,'guru']
# list.remove(100)
# list.append(255)
# print(list)
# print(type(list))
# it is heritogoues, mutables---------


# range-----------------------

# x=range(10)
# print(x)
# print(type(x))

# y=range(0,7,2)
# for i in y:print(i)
# print(y)

# string------------------------


# a='guru'
# print(a)
# print(type(a))


# c="gurucharan"
# d="""hello
#            world"""
# print(c)
# print(d)


# a="gURuchARAn"
# a='gurucba'
# a='guru8441390'
# print(a.capitalize())
# print(a.casefold())
# print(a.center(5))
# print(a.count('A'))
# print(a.endswith('a'))
# print(a.endswith('n'))
# print(a.find('A'))
# print(a.format())----**
# print(a.index('A'))
# print(a.islower())
# print(a.isdigit())
# print(a.isidentifier())
