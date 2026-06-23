'''
num = 5
1
1   2
1   2   3   
1   2   3   4
1   2   3   4   5

1
2   2
3   3   3   
4   4   4   4
5   5   5   5   5

1
2   3
4   5   6
7   8   9  10
11  12  13 14  15

'''
k = 1
for i in range(1,6): # i = 1  i = 2 i = 3
    for j in range(1,i+1):
        print(k,end="\t")
        k += 1
    print("\n")
        