a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
c=set(c)
d=set(d)
e=c.intersection(d)
print(len(e))