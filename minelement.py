n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
m=a[0]
for i in a:
    if i<m:
        m=i
print(m)