a,b= map(int,input().split())
c = list(map(int,input().split()))
d = list(map(int,input().split()))
e = []
for i in c:
    if i in d:
        if i not in e:
            e.append(i)
for j in d:
    if j in c:
        if j not in e:
            e.append(j)

            
print(len(e))