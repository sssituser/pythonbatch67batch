'''
Write a program to check given number is armstrong or not .
num = 153    1cube+5cube+3cube => 1+125+27=> 153
num = 1634   1pow4+6pow4+3pow4+4pow4 => 1634
'''
def isarmstrong(num):
    res = str(num)
    power = len(res) # power = 3
    sum = 0
    for digit in res: #  '153' digit = '1' digit = '5' digit = '3'
        sum = sum+ int(digit)**power # sum = 1 sum = 126 sum = 27+126 => 153
    return sum==num

print(isarmstrong(153))
print(isarmstrong(123))
print(isarmstrong(1634))