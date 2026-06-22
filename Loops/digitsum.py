num = int(input('Enter a number ' ))
sum = 0
copy = num
while num>0: 
    digit = num%10 
    sum = sum+digit 
    num = num//10 
print(f'Sum of the digits of {copy} is {sum}')
# num = 123   Avg = 1+2+3//3=> Avg = 2
    