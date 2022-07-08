n=int(input())
List=list(map(int,input().split()))
p=''
for i in List:
    p=p+str(i)
p=int(p)+1
Li=list(str(p))
print(*Li)
