
# #Class

# class Person:
#  pass
#     #Class Attirbutes

#  address='No Information'
#     #Constructor(Yapıcı Method)
#  def __init__(self,name,year):
  
#     #Object Attirbutes
#     self.name=name
#     self.year=year
#     print('Init Method is working well')

#     #Instance Methods

#  def intro(self):
#       print('Hello There')

#  def calculateAge(self):
#       return 2010 - self.year

# #Object(Instance)

# p1=Person('David ',2001)
# p2=Person('Star ',1999)

# p1.intro()
# p2.intro()

# print(f'My Name:{p1.name} and my age:{p1.calculateAge()}')
# print(f'My Name:{p2.name} and my age:{p2.calculateAge()}')

# #Updating Objects

# p1.name='Mason '
# p1.address='Ohio'

# #Accesing Objects
 
# print(f'name:{p1.name}year:{p1.year}address:{p1.address}')
# print(f'name:{p2.name}year:{p2.year}address:{p2.address}')

# print(type(p1))
# print(type(p2))

class Circle:
    #Class Object Attirbute
     pi=3.14
     def __init__(self,radius=1) :
          
    #Methods

    def perimeter_calculate(self,):
       return 2*self.pi+self.radius
    def area_calculator(self):
        return self.pi*(self*radius**2)
circle_01=Circle()
circle_02=Circle(7)

print('circle_01:Alan={circle_01.area_calculator()} Çevre={circle_01.perimeter_calculate}')
print('circle_02:Alan={circle_02.area_calculator()} Çevre={circle_02.perimeter_calculate}')