
#Class

class Person:
 pass
    #Class Attirbutes

 address='No Information'
    #Constructor(Yapıcı Method)
 def __init__(elf,name,year):
  
    #Object Attirbutes
    elf.name=name
    elf.year=year
    print('Init Method is working well')
    #Methods

#Object(Instance)

p1=Person('David ',2001)
p2=Person('Star ',1999)

#Updating Objects

p1.name='Mason '
p1.address='Ohio'

#Accesing Objects
 
print(f'name:{p1.name}year:{p1.year}address:{p1.address}')
print(f'name:{p2.name}year:{p2.year}address:{p2.address}')

print(type(p1))
print(type(p2))