num = input('Enter input : ')
num=num.lower()
if(num==num[::-1]):
    print(f'{num} given input is a Palindrome')
else:
    print(f'{num} given input is not a Palindrome')
    