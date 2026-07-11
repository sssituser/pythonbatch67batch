'''
The function calling its own function is called recursive function.
Write a program to find the sum of n numbers ?
num = 5         sum = 1+2+3+4+5 => 15
'''
def sum(num):
    if  num==0:
        return 0
    return num+sum(num-1)
num = 5
res = sum(num)
print(f'sum of {num} numbers is {res}')
'''
sum(5)=> 5+10 => 15
'''
