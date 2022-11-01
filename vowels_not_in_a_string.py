s=input()
v='aeiou'
c=0
for i in v:
    if i not in s:
        print(i,end=" ")
        c=1
if c==0:
    print(c)