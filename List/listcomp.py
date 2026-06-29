li = [1,2,3,1,5,6,1,3,6,7,8]
evens =[x for x in li if x%2==0]
print(evens)
odds =[x  if x%2 !=0 else "Even" for x in li]
print(odds)
divbythree =[x for x in li if x%3==0]
print(divbythree)
print(li)
print([5*x for x in li])