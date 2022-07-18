s=input().lower().split()
c=""
for i in s[0]:
    f=0
    for j in s[1:]:
        if i in j:
            f=1
        else:
            f=0
            break
    if f==1:
        c+=i
print(len(c))