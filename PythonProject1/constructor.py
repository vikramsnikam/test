class person:
    def __init__(self):
        print("Person constructor")

    def display(self):
        print("Person display")

obj1 =person()
print(1)
obj1.display()



print('argument constructor')
class goodperson:
    def __init__(self,age):
        print("goodperson constructor",age)

    def display(self):
        print("goodperson display")
obj3 =goodperson(20)
obj4=goodperson(25)


print('another')

class industry:
    def __init__(self,name,age):
         self.name=name
         self.age=age
    def display(self):
        print("empl name is" ,self.name," \n" "age is" ,self.age)


a=industry('john',20)
a.display()
b=industry('johny',25)
b.display()
