'''
    write program to find the sum of the digist of a given number.
    num = 123   sum = 6
    num = 456   sum = 15
'''

# def digitsum(num):
#     sum = 0
#     while num>0:
#         digit = num%10
#         sum  = sum+digit
#         num=num//10
#     return sum

def digitsum(num):
    res = str(num) # num = '123'
    sum = 0
    for char in res: # '123' char=1 char=2 char=3
        sum = sum + int(char) # sum = 0+1 => sum = 1 sum = 1+2 => sum = 3+3=> sum = 6
    return sum

num = 123
print(f'sum of the digits of a given nuber {num} is : {digitsum(num)}')