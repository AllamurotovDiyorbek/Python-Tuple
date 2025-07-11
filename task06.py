emails = (
    ("Ali", "ali@gmail.com"),
    ("Vali", "vali@yandex.ru"),
    ("Sami", "sami@mail.ru")
)
c = []
for name, email in emails:
    at_index = email.index("@")
    domain = email[at_index+1:]           
    c.append(domain)
print(c)