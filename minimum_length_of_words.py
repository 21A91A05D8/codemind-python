s=input().split()
minn=1000
for i in s:
    minn=min(minn,len(i))
print(minn)