tu = (45,67,89,23,44,66)

for index in range(len(tu)):# index = 0,1,2,3,4,5
    print(f'index - {index}  {tu[index]}')
    
    
for index in range(-1,-(len(tu)+1),-1):
    print(f'index -> {index}  {tu[index]}')
    
print(f'First three values {tu[0:3]}')

print(f'Last three values {tu[:-4:-1]} ')
    
    
   