A = {1,2,3,4}  
B = {'a','b','c',1,2}
print(A)
print(B)
c = A.union(B)
print(f'c = {c}')
x = {"abc","def","pqr",33}
y = {99,66,88,33}

z = x|y
print(z)

r = A.intersection(B)
print(r)

t = x&y
print(t)