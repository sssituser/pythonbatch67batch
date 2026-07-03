name = input('Enter Name : ')
alphas = "abcdefghijklmnopqrstuvwxyz"
res = ''
for k in name: # "abc"
    res+=alphas.__getitem__(25-alphas.index(k))
print(f'for the given string : {name} Encrpytion is {res}')