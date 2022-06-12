def rev(s):
    l=len(s)
    s1=''
    for j in range(l-1,-1,-1):
        s1+=s[j]
    return s1
s=input()
arr=list(s.split())
for i in arr:
    print(rev(i),end=" ")
