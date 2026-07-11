'''
Find the factorial of a given number using recursive function
num = 5   5! => 120
num = 4   4! => 24
'''
def factorial(num):    #function definition
    if num==0 or num==1:
        return 1
    return num*factorial(num-1)
num = 4
res = factorial(num)
print(f'{num}! is {res}')

# fact(5)=>5*24->120
