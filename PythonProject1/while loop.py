a=10
while a<20:
    print(a)
    a+=1

print("even odd with while loop")
b=2
while b<50:
    if b%2==0:
        print('e',b)
    else:
        print(b)
    b=b+1
#if remove condition b=b=1 it will create infinite loop
print('break using if')
k=10
for i in range (k):
    if i >5 :
        break
    else:
        print(i)

print('continue if')
k=10
s=[]
for i in range (k):
    if i==3:
       continue
    else:
        s.append(i)
print(s)

print('while break')
num=10
while num<15:
    print(num)
    num=num+1

print('continue while loop')
num=10
while num<15:
    num=num+1
    if num%2==0:
        continue
    print(num)

print('pass')
n=1
while n<10:
    if n%2==0:
        pass
    else:
        print(n)
    n=n+1
