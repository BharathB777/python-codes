n=int(input())
a=set()
while n!=1 and n not in a:
    a.add(n)
    s=0
    while n>0:
        r=n%10
        s+=r*r
        n//=10
    n=s
print("Happy Number" if n==1 else "Not Happy Number")
