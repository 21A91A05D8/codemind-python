s=list(input().split())
vo='AEIOUaeiou'
c=0
m=1000
for i in s:
    c=0
    for j in i:
        if j in vo:
            c+=1
    if(m>c):
       m=c 
print(m)