num = int(input('Enter a number : '))
rev = 0
copy = num
while num>0:
    digit=num%10
    rev = rev*10+digit
    num//=10
if copy == rev:
    print(f'{copy} is a Palindrome number')
else:
    print(f'{copy} is not a Palindorme number')