'''6---> 1-factor
6%1---> rem =0 sum = 1
6%2 --> rem = 0 sum = 3
6%3 --> rem = 0 sum = 6
6%4 --> rem =2
6%5 --> rem = 1
1.Take number
2. Repeat the loop from 1 to lessthan that number
3. divide the number from 1 to lessthan 6
4.if the remainder zero then add the factor to the sum
5. compare sum with number , if both are equal given number perfect
other wise perfect

'''
start = 1
num = int(input('Enter a number: '))
sum = 0
while start<num: # 1<6-T 2<6-T 3<6 4<6-T 5<6-T 6<6-F
    if num%start == 0: # 6%1-> 0==0-T 6%2->0==0-T 6%3->0 == 0-T 6%4->2==0-F 6%5->1==0-F
        sum = sum+start # sum = 0+1=> sum = 1 sum = 3 sum = 6
    start += 1 # start = 2 start = 3 start = 4 start = 5 start = 6
if sum == num:
    print(f'{num} is a Perfect number')
else:
    print(f'{num} is not a Perfect number')
    

