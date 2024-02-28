
#Inheritance(Miras)

class Person():
    def __init__(self,first_name,surname):
        self.FirstName=first_name
        self.LastName=surname
        print('Person Created.')

    def who_am_i(self):
        print('I am a person')

    def eat(self):
        print('I am eating')

class Student(Person):
    def __init__(self,first_name,surname,stu_number):
        super().__init__(first_name, surname)
        self.StudentNumber=stu_number
        print('Student Created')

    def who_am_i(self):
        print('I am a student')

class Teacher(Person):
    def __init__(self, first_name, surname,branch):
        super().__init__(first_name, surname)
        self.Branch=branch

    def who_am_i(self):
        print(f'I am a {self.Branch} teacher')

p1=Person('Stella','Johnson')
s1=Student('Jordan','Dawson',1521)
t1=Teacher('Abraham','Clinton','Math')

print(p1.FirstName+' '+p1.LastName)
print(s1.FirstName+' '+s1.LastName+' '+str(s1.StudentNumber))

p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
s1.sayHello()
t1.who_am_i()
t1.eat()