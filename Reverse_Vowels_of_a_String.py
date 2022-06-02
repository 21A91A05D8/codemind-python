s=list(input())
v='aeiouAEIOU'
vow=''
for i in s:
    if i in v:
        vow+=i
vow=vow[::-1]

j=0
for i in range(len(s)):
    if s[i] in v:
        s[i]=vow[j]
        j+=1
print("".join(s))