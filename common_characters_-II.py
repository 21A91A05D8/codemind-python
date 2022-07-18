s1 = input().lower()
s2 = input().lower()
s1=s1.replace(" ","")
s2=s2.replace(" ","")
a = ''
for i in s1:
    if i in s2 and i not in a:
        a+=i
for i in s2:
    if i in s1 and i not in a:
        a+=i
a=sorted(a)
print(len(a))