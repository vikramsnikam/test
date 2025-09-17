c=14

def num1():
    #c+=10 will not work because we cant change global value inside function
    print(c)
num1()

#to change global value inside function use global keyword
c=67
def num2():
    global c
    c+=3
    print(c)
num2()