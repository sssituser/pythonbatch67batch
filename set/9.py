s = {78,90,34,56}
fr = frozenset(s)
print(f's = {s}\t fr = {fr}')
s.add(100)
#fr.add(100)
print(f's = {s}\t fr = {fr}')
print(dir(fr))

