'''
    Write a program to generate the number from 1 to given number ?
    Example : num = 5   res = 1,2,3,4,5,
        1.def    2.GenNumbers      3.Parameters num     5. string
'''
def GenNumbers(num:int):
    res = ''
    for i in range(1,num+1):
        res += str(i)+","
    return res[0:len(res)-1]+"."

x = GenNumbers(5)
print(x)

print(GenNumbers(10))

# 1,3, 5, 7, 9, 11, 13, 15.
# 2,4,6,8,10.
# 1,4,9,16,25,36.