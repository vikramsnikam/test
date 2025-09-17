a=[1,2,3,4,5]
#create list with double value of original list
a2=[num*2 for num in a]
print(a2)

b=['a','b','c']
b2=[num*3 for num in b]
print(b2)

c=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
even=[num for num in c if num%2==0]
print(even)
even=[num for num in range (1,10)if num % 2 == 0]
print(even)
odd=[num for num in c if num%2!=0]
print(odd)


print('finding common character in string')
a='chlorine'
b='bromine'
c=[char for char in a if char  in b]
print(c)

