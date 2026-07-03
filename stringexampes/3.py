name = input('Enter Name : ')
alphabets = "abcdefghijklmnopqrstuvwxyz"
sum = 0

for k in name: # name = "abc"
    sum = sum+alphabets.index(k)+1 # sum = 1   
print(f'{name} score is {sum}') 


