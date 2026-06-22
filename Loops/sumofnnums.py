num = 5
start = 1
end = num
sum = 0
while start<=end:# 1<=5 -T 2<=5-T 3<=5 4<=5 5<=5-T 6<=5-F
    print(start) # start = 1 2 3 4 5
    sum = sum+start # sum = 0+1=> sum = 1 sum = 3 sum = 6 sum = 10 sum = 15
    start= start+1  # start = 2 start = 3 start = 4 start  = 5 start = 6
print(f'sum of {num} numbers is {sum}')