n=int(input())
a=list(map(int,input().split()))
c=0
l=[]
for i in sorted(set(a),key=a.index):
    if a.count(i)==i:
        l.append(i)
        c+=1
if c==0:
    print("-1")
else:
    print(min(l),max(l))
    