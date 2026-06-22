num = int(input("Enter a number : "))
count = 0
sum = 0
copy = num
while num>0:
    digit = num%10
    count += 1
    sum += digit
    num //=10
avg =sum//count
print(f'Average of the digits of a given number {copy} is {avg}')