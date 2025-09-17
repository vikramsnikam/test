global_a=10
def fun1():
    outer_a=20
    def fun2():
        inner_a=30
        print(inner_a)

    print(outer_a)
    fun2()
print(global_a)
fun1()


print('closure')
def a():
    name='jon'
    def b():
        print('hi'+name)
    b()

print(a())

print('decorator')
def multiply(x,y):
    return x*y
def add(x,y):
    return x+y
def cal(act,x,y):
    return act(x,y)

result=cal(multiply,10,20)
rsult=cal(add,10,20)
print(result)
print(rsult)

print('regex')
import re

pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")





