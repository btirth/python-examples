
f1 = open('tirth.txt',"r")
f2 = open('bharatiya.txt',"w")

print(f1.read())  #to print whole file
print()

f1.seek(0)        #to reset pointer to beginning
print(f1.readline()) #to print 1st line of file
print(f1.readline()) #to print 2nd line of file
print(f1.readline(4)) #to print 4 character of 3rd line of file

f2.write('Hi...Tirth')
f2.write('')


