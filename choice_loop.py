number1=int(input("number1= "))
number2=int(input('number2= '))
print("1.add")
print("2.subtract")
print("3.multiplication")
print("4.division")
print("5.exit")
choice=int(input("enter choice="))
while (choice!=5):
    if choice==1:
        result=number1+number2
    elif  choice==2:
        result=number1-number2
    elif  choice==3:
        result=number1*number2
    elif  choice==4:
        result=number1/number2
    else:
        print("invalid choice")
    print(result)
print("Thank you")
