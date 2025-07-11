numbers = (3, 6, 7, 8, 10, 11)
c=[]
for i in numbers:
    if i%2==0:
        c.append(i)
print(tuple(c))