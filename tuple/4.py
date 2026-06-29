tu = (56,78,34,23)

evens = [x for x in tu if x%2==0]
print(evens)

evenoddtext =["even" if x%2==0 else "odd" for x in tu]
print(evenoddtext)

print(len(tu),max(tu),min(tu),sum(tu))

