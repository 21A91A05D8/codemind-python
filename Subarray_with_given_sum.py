def subarray(a,b,c):
    for i in range(a):
        summ=c[i]
        for j in range(i+1,a+1):
            if summ==b:
                print("%d %d"%(i+1,j))
                return 1
            if summ>b or j==a:
                break
            summ+=c[j]
    print('-1')
for _ in range(int(input())):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    subarray(a,b,c)
    