n=int(input())
li=list(map(int,input().split()))
lis=[]
for i in li:
    if i not in lis:
        lis.append(i)
print(*lis)
