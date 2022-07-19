a=input().split()
m=10000
for i in a:
    m=min(len(i),m)
print(m)