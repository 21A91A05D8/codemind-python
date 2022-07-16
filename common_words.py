a=input()
b=input()
a=a.lower()
b=b.lower()
a=a.split()
b=b.split()
for i in range(0,len(b)):
    if b[i] in a:
        print(b[i],end=' ')