n=int(input())
a=list(map(int,input().split()))
m=int(input())
s=[]
if m not in a:
    s.append(-1)
    s.append(-1)
for i in range(len(a)):
    if m==a[i]:
        s.append(i)
        break
for i in range((len(a)-1),-1,-1):
    if m==a[i]:
        s.append(i)
        break
print(*s)
    