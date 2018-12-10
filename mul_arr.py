import array as arr

x=arr.array('i',[])
n=int(input('Enter the length of array = '))

for i in range(n):
    a=int(input())
    x.append(a)

for i in range(n-1):
    print(f"{x[i]} + {x[i+1]} = {x[i]+x[i+1]}")
    
