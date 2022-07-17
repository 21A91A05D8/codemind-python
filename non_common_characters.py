a=input().lower()
b=input().lower()
a=a.replace(" ","")
b=b.replace(" ","")
s=''
for i in a:
    if i not in b and i not in s:
        s+=i
for i in b:
    if i not in a and i not in s:
        s+=i
s=sorted(s)
s=''.join(s)
print(s)