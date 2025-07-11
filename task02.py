students = [("Ali", ["Fizika", "Matematika"]), ("Laylo", ["Ingliz tili"]), ("Jasur", ["Matematika", "Informatika"])]
c=0
for i in students:
    if "Matematika" in i[1]:
        c+=1
print(f"{c} talaba Matematika fannini tanlagan")