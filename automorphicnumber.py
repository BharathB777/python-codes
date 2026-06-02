n=int(input())
x=n*n
if str(x).endswith(str(n)):
    print("Automorphic")
else:
    print("Not Automorphic")