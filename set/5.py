s = {56,78,23,99}
s.discard(23)
print(s)
print(f'Deleted element is : {s.pop()}')
print(s)
s.clear()
print(s)
#print(s.pop())# keyerror
#s.remove(56)
s.discard(56)
print(s)
'''
    If the elements are not present in the set, if we try to delete from the 
    set using pop ,remove methods can return key error, where discard
    will not return any error.
'''
