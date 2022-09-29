s=int(input())
x=ord('A')+(s-1)
for i in range(s,0,-1):
    for j in range(0,i):
        print(chr(x),end=' ')
    x-=1
    print()
    
        