n=int(input())
for j in range(n):
    for i in range(1,n-1):
        print(i,end="")
    for i in range(n-3,0,-1):
        print(i,end="")
    print()