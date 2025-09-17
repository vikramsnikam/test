class student:
    a=10
    def display(self):
        print('student')
        return 'sd'

class teacher(student):
#if we create display file here will not give value of student class
    def disp(self):
     super().display()

     return 'teacher'

obj = teacher()
print(obj.display())

print('super function')
print(obj.disp())



print('multiple inheritance')
class army:
    def role(self):
        print('army defend land')

class airforce:
    def task(self):
        print('airforce defend sky')

class defence(army, airforce):
    pass
s1=defence()
s1.role()
s1.task()

print('multilevel inheritance')
class airforce:
    def task(self):
        print('airforce defend sky')
class defence(airforce):
    pass

class commercial(airforce):
    pass

d1=commercial()
d1.task()
