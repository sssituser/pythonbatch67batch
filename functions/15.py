'''
num = 123    sum = 1+2+3 => 6
             mul = 1*2*3 => 6
123 spy number
'''
# def isspynumber(num): # num = 123
#     s = str(num)
#     mul = 1
#     sum = 0
#     for i in s: # i = '1' i = '2' i = '3'
#         sum = sum+int(i) # sum = 1 sum = 1+2=>3 sum = 6
#         mul = mul*int(i) # mul = 1 mul = 1*2=> 2*3 mul = 6
#     return sum==mul

def isspynumber(num):
    sum = 0
    mul = 1
    while num>0:
        digit =  num%10
        sum = sum+digit
        mul = mul*digit
    return sum==mul

print(isspynumber(123))
print(isspynumber(146))
