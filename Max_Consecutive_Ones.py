n=int(input())
nums=list(map(int,input().split()))
c=0
maxx=0
for i in nums:
    if i==1:
        c+=1
        maxx=max(c,maxx)
    else:
        c=0
print(maxx)































