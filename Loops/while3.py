'''
Write a program to generate odd numbers for the givenumber
10
1 3 5 7 9
20
1 3 5 7 9 11 13 15 17 19
'''
start = 1
end = int(input('Enter a number : '))
while start<=end:
    print(start,end=" ")
    start = start+2