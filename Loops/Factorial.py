start = 1
num = int(input('Enter a number : '))
fact = 1
while start<=num: 
    fact = fact*start 
    start = start+1 
print(f'{num}! is :{fact}')    