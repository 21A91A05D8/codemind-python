n = input().lower()
n = n.replace(" ","")
s = []
for i in range(0,len(n)):
    c = n.count(n[i])
    if c==1:
        s.append(n[i])
s.sort()
s="".join(s)
print(s)