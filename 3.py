t_1=(1,4,9,16,25,36)
l=[]
for i in t_1:
    a=i*i
    l.append(a)
t_modified = tuple(l)
t_sliced = tuple(l[1:4])
print(t_1)
print(t_modified)
print("Element at index position 4 of t_modified : ",t_modified[4])
print(t_sliced)