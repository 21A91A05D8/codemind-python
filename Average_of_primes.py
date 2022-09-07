def isPrime(p):
    c=0
    for i in range(1,p+1):
        if p%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
n=int(input())
arr=list(map(int,input().split()))
s=0
l=0
for i in arr:
    if isPrime(i):
        s+=i
        l+=1
print("%.2f"%(s/l))