s=int(input())
p=sp=0
for i in range(s):
    arr=list(map(int,input().split()))
    for j in range(s):
        if i==j:
            p+=arr[j]
        if i+j==s-1:
            sp+=arr[j]
print("Principal Diagonal:",end='')
print(p)
print("Secondary Diagonal:",end='')
print(sp)