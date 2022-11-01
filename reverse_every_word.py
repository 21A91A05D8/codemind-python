s=input().split()
p=[]
for i in s:
    p.append(i[::-1])
print(" ".join(p))