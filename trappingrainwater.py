n=int(input())
a=list(map(int,input().split()))
w=0
for i in range(n):
    l=max(a[:i+1])
    r=max(a[i:])
    w+=min(l,r)-a[i]
print(w)