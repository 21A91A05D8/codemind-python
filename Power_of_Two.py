x=int(input())
sum=1
i=0
h=0
while(sum<=x):
    sum=2**i
    if(sum==x):
        print("True")
        h=1
        break
    i+=1
if(h==0):
    print("False")