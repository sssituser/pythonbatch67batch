finame = input('Enter File Name')
file = open(finame,mode='w+')
x = input("Enter Your Information : ")
while x !='':
    file.write(x)
    x=input()
    
