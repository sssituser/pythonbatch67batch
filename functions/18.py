'''
Adam number

num = 12    numsq = 144
revnum = 21 revnumsq = 441   rev=144


'''
def square(num):
    return num*num

def reverse(num):
    res = str(num)
    return int(res[::-1])
    
def isaadam(num): # num = 12
    return square(num) ==   reverse(square(reverse(num)))
 
    


print(isaadam(10))
print(isaadam(11))
print(isaadam(12))




