'''
Write a program to generate list amstrong numbers for the
given range.

num = 100  end = 1000   153  370  371 407
'''
def isarmstrong(num): # 153  1cube+5cube+3cube 1634 1pow4+6pow4+3pow4+
   s = str(num)
   power =  len(s)
   copy = num
   sum = 0
   while num>0: #153
       digit = num%10
       sum += digit**power
       num = num//10
   return sum == copy
       
    
def getarmstrongs(start,end):
    res = ""
    for num in range(start,end+1):
        if isarmstrong(num):
            res += str(num)+","
    return res[0:len(res)-1]+"."

print(getarmstrongs(100,10000000))