n=input().lower()
n=n.replace(" ","")
s=[]
for i in n:
    c=n.count(i)
    if c==1:
        s.append(i)
print(len(s))