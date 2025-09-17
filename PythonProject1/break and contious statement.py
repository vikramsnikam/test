a=['a','b','c','d','e']
for i in a:
    if(i=='c'):
        break
    else:
        print(i)


print('D')
b=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in b:
   if(i>6):
       print(i)

print('using else')
b=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in b:
    if(i>6):
            break
    else:
        print(i)

print('continuous statement')

b=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in b:
    if(i==6):
        continue
    else:
        print(i)


print('nested loops')
a=['a','b','c','d','e']
for i in range (0,5):
    print(i)
    for j in a:
        print(j)

