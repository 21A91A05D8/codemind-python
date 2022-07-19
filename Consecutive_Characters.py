s=input()
m=1
n=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        m+=1
        n=max(n,m)
    else:
        m=1
print(n)