print('calculator using function')
def add(a,b):
     print(float(a) + float(b))
def sub(a,b):
    print(float(a) - float(b))
def mult(a,b):
    print(float(a) * float(b))
def div(a,b):
    print(float(a) / float(b))
def power(a,b):
    print(float(a) **float(b))
a = input('enter a number')
b = input('enter a second number')
c = input('enter a operation')

if c=='+':
    add(a,b)
if c=='-':
    sub(a,b)
if c=='*':
    mult(a,b)
if c=='/':
    div(a,b)
if c=='**':
    power(a,b)