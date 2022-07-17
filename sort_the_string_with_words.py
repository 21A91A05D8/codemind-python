n=list(map(str,input().split()))
for i in range(len(n)):
    for j in range(len(n)):
        if i!=j and n[i]<n[j]:
            temp=n[i]
            n[i]=n[j]
            n[j]=temp
print(*n)