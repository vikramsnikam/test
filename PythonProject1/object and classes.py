class carbon:
    graphite="random"
    graphene="2d"
    diamond="3d"
    c60="multi"


print(carbon)

obj=carbon()
print(obj.graphite)
print(obj.graphene)
print(obj.diamond)
print(obj.c60)
# can create multiple objects from class obj2, obj3
objtwo=carbon()
#changing name of class
objtwo.graphite='coal'
print(objtwo.graphite)
print(objtwo.graphene)
print(objtwo.diamond)

print('adding/updating item in clas')
objtwo.symbol="c"
print(objtwo.symbol)

print('class method')
class student:
  def display(self,a):
        print("id",a)
std=student()
std.display(1)
std.display(2)


print('area calculation')
class room:
    length=0.0
    width=0.0
    def calculate(self):
        print("area",self.length*self.width,)

area=room()
area.width=56
area.length=90
area.calculate()


print('constructor')
class croom:
    def __init__(self,name,age):
        print(" call constructor")
        self.name=name
        self.age=age
    def display(self):
        print(" call name")

obj=croom('c',20)
print(obj.name)
print(obj.age)
obj.display()

obj1=croom('d',24)

print(obj1.name)
print(obj1.age)
obj1.display()












