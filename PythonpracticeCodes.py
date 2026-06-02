"""1. Rotate Array by K Positions"""
n=int(input())
a=list(map(int,input().split()))
k=int(input())
k=k%n
a=a[-k:]+a[:-k]
print(*a)


"""2. Longest Common Prefix"""
n=int(input())
a=[]
for i in range(n):
    a.append(input())
p=a[0]
for s in a[1:]:
    while not s.startswith(p):
        p=p[:-1]
        if p=="":
            break
if p:
    print(p)
else:
    print(-1)
    
    
"""3. Minimum Window Substring"""
s=input()
t=input()
m=""
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        x=s[i:j]
        ok=True
        for c in t:
            if x.count(c)<t.count(c):
                ok=False
                break
        if ok:
            if m=="" or len(x)<len(m):
                m=x
print(m)


"""4. Electricity Bill"""
u=int(input())
if u<=100:
    b=u*2
elif u<=300:
    b=u*3
else:
    b=u*5
print(b)


"""5. Employee Bonus"""
s=int(input())
r=int(input())
if r>=90:
    b=s*20//100
elif r>=75:
    b=s*10//100
else:
    b=s*5//100
print(b)


