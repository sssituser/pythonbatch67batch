'''
Write a program to find the charcter frequecy of the given name
example : "abbccdd"
{"a":1,"b":2,"c":2,"d":2}
'''
name = input('Enter Name : ') # aabc
cf = {}
for i in range(len(name)): # i = 0 i = 1 i = 2 i = 3
    if cf.__contains__(name[i]): 
     val = cf[name[i]]
     cf[name[i]] = val+1
    else:
        cf[name[i]] = 1 # {"a":2,"b":1,"c":1}
print(cf)

name