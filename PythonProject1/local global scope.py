print('local')
def num():
    a=10
    print(a)
num()
#print(a) will not work because a is defined inside function


print('global')
b=56
def num():
    print('local',b)
num()
print('global',b)

print('nonlocal')
def num():
    a=10
    print(a)
    def num1():
        print("num1",a)
    def num2():
          a=34
          print('num2',a)
    num1()
    num2()
num()
#here a=10 in function num and num 2 but inside num 1 it will be 34 because we redefined in num1
#will show a=34 if we write any function inside nu1


