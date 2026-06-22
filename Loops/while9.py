'''
Write a program to generate multiplcation table for the given number.
num = 5
5 x 1 = 5

5 x 10 = 10
'''
start = 1
end = 10
num = int(input('Enter a number : '))
while start <=end:#1 <=10-T
    print(f"{num} x {start} = {num*start} ")
    start = start+1