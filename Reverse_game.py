def rev(n):
    r = 0
    while n:
        r=r*10+n%10
        n//=10
    return r

n = int(input())
arr = list(map(int,input().split()))
for i in range(n):
    print(rev(arr[i]),end=" ")