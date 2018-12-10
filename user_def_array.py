from array import *

x=array('i',[])

n=int(input('Enter the length of array  '))
print()

print('enter the elements of array  ')
for i in range(n):
    a=int(input())
    x.append(a)


print(x)
