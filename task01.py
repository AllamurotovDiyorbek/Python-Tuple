people = [("Ali", 24), ("Laylo", 30), ("Jasur", 19)]
a=people[0][1]
for i in people:
    if a<i[1]:
        a=i[1]
print(a)