words = ("apple", "banana", "strawberry", "kiwi")
c=len(words[0])
d=str
for i in words:
    if len(i) > c:
        c=len(i)
        d=i
print(d)