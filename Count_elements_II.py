a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
#c=set(c)
#d=set(d)
e=0
for i in list(set(c)):
    if d.count(i)==0:
        e+=1
for j in list(set(d)):
    if c.count(j)==0:
        e+=1
print(e)