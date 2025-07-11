orders = [(102, "Ali"), (99, "Vali"), (150, "Sami")]
c=[]
for i in orders:
    if i[0]%2==0:
        c+=i
print(c)