num = int(input('Enter a number : '))
start = 1
while start<=num:
    j = 1
    while(j<=start):
        print(j,end="\t")
        j+=1
    print()
    start += 1
num-=1
while num>=1:
    j=1
    while(j<=num):
        print(j,end="\t")
        j+=1
    print()
    num-=1
        