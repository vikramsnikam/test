"using if"
a=[1,2,3,4,5,6,7,8,9,10,11,12]
#for even nos.
for i in a:
    if(i%2==0):
        print("e",i)

# for odd nos.
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for i in b:
     if (not(i%2==0)):
        print('odd',i)

"using if else"
c=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in c:
    if (i%2==0):
        print("e",i)
    else:
        print("odd",i)

print('separating creating list even and odd')
a=[1,2,3,4,5,6,7,8,9,10,11,12]
odd=[]
even=[]
for i in a:
 if (i % 2 == 0):
    even.append(i)
 else:
    odd.append(i)

print('even', even)
print('odd', odd)


print("loop through string")

name='vikram'
for i in name:
    print(i)

print("loop through list", 'creating list from string')
name='vikram'
a=[]
for i in name:
        a.append(i)
print(a)


print("range loop", )

for i in range(0,15) :
    print(i)


