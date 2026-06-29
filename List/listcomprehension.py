li =[67,89,34,56,23,12,45,67,89]


evens= [x for x in li if x%2==0]
print(evens)

evenoddli=[f"{x}<-Even" if x%2==0 else f"{x}<-Odd" for x in li]
print(evenoddli)


mulof7 =[x for x in li if x%7==0]

print(mulof7)