'''
num = 153   1cube+5cube+3cube => 1+125+27=> 153
num = 1634  1pow4+6pow4+3pow4+4pow4=> 1634

Steps :
1.Take num
2. Count digit
3. Separate the digit
4. Find the Power Values
5. Sum power values
6. compare original number to sumof the power value
7. If both are equal Original number is Armstrong number other wise not an Armstrong number
'''

num = int(input('Enter a number : '))
copy = num
count = 0
while num>0: 
    digit = num%10 
    count  = count+ 1 
    num  = num//10  
num = copy
sum = 0
while num>0: 
    digit = num%10 
    sum = sum + digit**count 
    num = num//10  
if copy==sum:
    print(f'{copy} is an Armstron number')
else:
    print(f'{copy} is not an Armstrong number')  






