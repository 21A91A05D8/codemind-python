for _ in range(int(input())):
    s=input()
    s=s[::-1]
    anu=0
    su=0
    for i in s:
        i=int(i)
        su+=i*(2**anu)
        anu+=1 
    print(su)