'''
num = 6
A
B   C
D   E   F
G   H   I   J
K   L   M   N   O    
P   Q   R   S   
T   U   V
W   X
Y

ASCII   
'''
num = 5
k = 97 # instead of 97 if we give 65 we get Upper Alphas
for i in range(1,num+1):
    for j in range(1,i+1):
        print(chr(k),end="\t")
        k+=1
    print()
for i in range(num-1,0,-1):
    for j in range(1,i+1):
        print(chr(k),end="\t")
        k+=1
    print()