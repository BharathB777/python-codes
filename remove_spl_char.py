s = input()
r = ""

for i in s:
    if i.isalnum() or i == " ":
        r += i

print(r)