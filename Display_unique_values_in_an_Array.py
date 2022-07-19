n=int(input())
a=list(map(int,input().split()))
f=0
for i in a:
    if a.count(i)==1:
        print(i,end=" ")
        f=1
if f==0:
    print("-1")