a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=0
for i in d:
    if i in c:
        c.remove(i)
        e+=1
if e==b:
    print("Yes")
else:
    print("No")