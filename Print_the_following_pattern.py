n=int(input())
n1=1
for i in range(n,0,-1):
    for j in range(1,n+1):
        if(j==n1 or j==i):
            print(i,end=" ")
        else:
            print(" ",end="")
    print("")
    n1+=1