a = int(input("Enter number1 "))
b = int(input("Enter number2 "))
print()
try:
    print(a/b)
    
except ZeroDivisionError as e:
    print("you can't devided by zero ",e)

except ValueError as e:
    print("Value Error")

except Exception as e:
    print(e)

finally :
    print()
    print("Bye...Bye")


