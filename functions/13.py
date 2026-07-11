'''
Write a program to check given number is Palindrome or not ?
'''
# def reverse(num):
#     rev = 0
#     while num>0:
#         digit = num%10
#         rev = rev*10+digit
#         num=num//10
#     return rev
# def ispalindrome(num): #123
#    return num==reverse(num)

def ispalindrome(input):
    input=str(input).lower()
    return input==input[::-1]
print(ispalindrome(123))
print(ispalindrome(121))
print(ispalindrome("eye"))

