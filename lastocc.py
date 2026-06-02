n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
x=int(input())
for i in range(n-1,-1,-1):
    if a[i]==x:
        print(i)
        break