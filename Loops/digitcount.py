num = int(input('Enter num : '))
count = 0
copy = num
while num>0: 
    digit = num%10
    count += 1 
    num = num//10 
print(f"{copy} has Total {count} Digits")    