s=input()
c=0
v='AEIOUaeiou'
co="qrtypsdfghjklzxcvbnmQWRTYPLKJHGFDSZXCVBNM"
i=0
j=len(s)-1
while(i<j):
    if((s[i] in v and s[j] in co) or (s[i] in co and s[j] in v)):
        c+=1
    i+=1
    j-=1
print(c)