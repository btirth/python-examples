x=int(input('Enter Number = '))
flag=True
for i in range(x):
    if x%i==0 :
        flag = False
        break

if flag==True :
    print('Prime Number')
else :
    print('Not Prime Number')
