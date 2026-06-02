s=int(input())
e=int(input())
for n in range(s,e+1):
    x=n
    d=len(str(n))
    t=n
    sm=0
    while t>0:
        r=t%10
        sm+=r**d
        t//=10
    if sm==x:
        print(x,end=" ")