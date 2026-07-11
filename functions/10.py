'''
Write a program to find the lucky number to the given date birth.
1-Oct-1990 => 1+10+1990 =>2001=>2+0+0+1=>3
3 Lucky Number
1.Take the date 
2.split dob  [1,oct,1990]
3.convert MothText to Number 10
4. date=1 month = 10 year = 1990
5. sum = date+month+year=> 2003
6. sum>9 => sum of the digits of given 2+0+1+8 => 11->1+1=>2

'''
def digitsum(num): #123
    sum = 0
    while num>0:
        digit = num%10
        sum+=digit
        num//=10
    return sum
def convertmonthtextonum(monthtext): # January
    monthtext=monthtext.lower()
    months = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
    for i in range(len(months)):
        if monthtext.__contains__(months[i]):
            return i+1
    return 0
        
        
dob = '9-Decementer-2008'
def getluckynum(dob):
    res = dob.split('-')
    date =  int(res[0])
    month = convertmonthtextonum(res[1])
    year = int(res[2])
    sum  = date+month+year
    while sum>9:
        sum = digitsum(sum)
    return sum

print(f'for the given {dob} lucky number is :{getluckynum(dob)}')