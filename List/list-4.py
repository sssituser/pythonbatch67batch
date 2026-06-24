li = [34,56,78,90]

print(li.__len__()) # 4  predefined function list
print(len(li)) # 4 predefined function 
for element in li:
    print(element)

for i  in range(len(li)):
    print(f'{i}----->{li[i]}')
    
for i in range(len(li)):
    print(f'li[{i}] ---> {li[i]}')
    
for i in range(-4,0):
    print(f'{i}  ===> {li[i]}')
    
for i in range(-4,0):
    print(f'li[{i}]  ===> {li[i]}')
    
for i in range(-1,-(len(li)+1),-1):
    print(f'li[{i}]==>{li[i]}')