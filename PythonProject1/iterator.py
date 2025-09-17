a={1,2,3,4,5,6,7,8,9,10,11,12}

b=iter(a)
print(b)
print(next(b))
#give next value
print(next(b))
#give next value3-9
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))

print('infinite iterator')
from itertools import count
a=count(1)
for i in range(10):
    print(next(a))