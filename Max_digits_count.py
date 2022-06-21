a=int(input())
b=list(input().split())
ma=0;c=0
for i in b:
    if len(i)>ma:
        ma=len(i)
for i in b:
    if len(i)==ma:
        c+=1
print(c)