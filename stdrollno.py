n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
x=int(input())
for i in range(n):
    if a[i]==x:
        print("Roll Number Found at Index",i)
        break
else:
    print("Roll Number Not Found")
    