a=input().lower().split()
b=input().lower().split()
c=0
for i in a:
    if a.count(i)==1 and b.count(i)==1:
        c+=1
print(c)