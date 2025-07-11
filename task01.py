people = [("Ali", 24), ("Laylo", 30), ("Jasur", 19)]
a=people[0][1]
c=str
for i in people:
    if a<i[1]:
        c=i[0]
        a=i[1]
print(f"{c} - {a} yosh")