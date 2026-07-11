'''
Write a program to generate list of palindrome number for the
given number.
start = 10      end = 100
PalindromeList : 11,22,33,44,55,66,77,88,99.
start = 100     end =1000
101,111,121,131,141.......999.

'''
def isPalindrome(num):#123
    copy = str(num)
    return copy==copy[::-1]

def getpalindromes(start,end):# start=100 end = 1001
    res = ""
    for num in range(start,end+1):
        if isPalindrome(num):
          res +=  str(num)+","
    return res[0:len(res)-1]+".";

print(getpalindromes(100,1000))