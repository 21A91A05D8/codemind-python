n=int(input())
a=list(map(int,input().split()))
k=int(input())
c=0
for i in sorted(set(a),key=a.index):
      if a.count(i)==k:
        print(i,end=" ")
        c = 1
if c==0:
    print("-1")