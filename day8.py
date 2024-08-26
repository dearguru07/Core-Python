# x=int(input("enter a number"))
# print(x)


# x,y=input("enter a numbre ").split()
# print(x)
# print(type(x))
# print(y)
# print(type(y))


# for taking the mutliple values as a input------------

# x,y=[int(x) for x in input("enter a number: ").split()]
# print(x)
# print(type(x))
# print(y)
# print(type(y))


# how to take the list as a input-----------------

# z=[int(x) for x in input("enter a number: ").split()]
# print(z)
# print(type(z))


# ( eval ) is accepts the any value as a inpout in list------------

# z=[eval(x) for x in input("enter a number: ").split()]  
# print(z)
# print(type(z))


# format----------------

# name="Guru"
# salary=85000

# print('Hey {x} ur salary is {y} '.format(x=name,y=salary))  =====> ( argments is x and y ) // {} is the replacement opeerator


# str mutliple and concatinacing----

# print('Guru'*5)
# print('Guru'+'charan')
# print('Gurucharan', end='P')
# print(10,20,30,50,sep=':')


# Higher functions : Higher order is a function , which is takes function as a argment-----


# map() & filter() & reduce()----------


# x=[1,5,10,20,30]

# def double(m):
#     return m*2
# y=list(map(double,x))
# print(y)

# map function op will always list - -----------

# x=[1,5,10,20,30]

# y=list(map(lambda s:s*s,x))
# print(y)


# filter()------------------------

# x=[1,5,55,65,7,8,955,10,20,3,0]
# y=list(filter(lambda s:s>10,x))
# print(y)

# x=[10,2,5,5,8,5,7,458,36,94,44,78,0,5,47]
# y=list(filter(lambda s:s>15,x))
# print(y)

# reduce-------------

# import reduce
# x=[10,2,5,5,8,5,7,458,36,94,44,78,0,5,47]
# y=list(reduce(lambda x,y:x if x>y else y,z))
# print(y)