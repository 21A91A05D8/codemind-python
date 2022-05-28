s=input().split()
maxx=0
for i in s:
    maxx=max(maxx,len(i))
print(maxx)