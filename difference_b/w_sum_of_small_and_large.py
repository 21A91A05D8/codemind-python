a=input().split()
s=ss=0
for i in a:
    mi=ord(max(i))
    s+=mi   
    ma=ord(min(i))
    ss+=ma
print(abs(ss-s))