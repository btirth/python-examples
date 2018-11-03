def sum_of_divisor(number):
    sum=0
    for i in range(1,number+1):
        if number%i==0:
            sum=sum+i
    print(sum)
