s={'A','B','C','D'}
s2={'A',2,'C',4}
forzen_set_1=frozenset(s)
forzen_set_2=frozenset(s2)
forzen_set_union=frozenset(s.union(s2))
forzen_set_common=frozenset(s.intersection(s2))
forzen_set_difference=frozenset(s.difference(s2))
forzen_set_distinct=frozenset((s.difference(s2)).union(s2.difference(s)))

print(forzen_set_1)
print(forzen_set_2)
print(forzen_set_union)
print(forzen_set_common)
print(forzen_set_difference)
print(forzen_set_distinct)