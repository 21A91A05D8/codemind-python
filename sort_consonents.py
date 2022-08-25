s=input().split()
for i in range(len(s)):
    p=list(s[i])
    for j in range(len(p)):
        for k in range(j+1,len(p)):
            if(p[j]>p[k] and p[j] not in 'AeiouaEIOU' and p[k] not in 'aeiouAEIOU'):
                p[j],p[k]=p[k],p[j]
    p=str(p)
    p = p.replace("[","")
    p = p.replace("]","")
    p = p.replace(" ","")
    p = p.replace(",","")
    p = p.replace("[","")
    p = p.replace("'","")
    print(p,end=" ")