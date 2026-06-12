n=input()
c=0
v=0
d=0
sc=0
so=n.lower()
for char in n:
    if char.isalpha():
        if char in "aeiou":
            v+=1
        else:
            c+=1
    elif char.isdigit():
        d+=1
    else:
        sc+=1
print(f"Vowels:{v}")
print(f"Consonants:{c}")
print(f"Digits:{d}")
print(f"Special Characters:{sc}")
