n=int(input())
if(n==0):
    print(0)
a=0
b=1
c=a+b
while (c<=n):
    a=b
    b=c
    c=a+b
if(abs(c-n)==abs(b-n)):
    print(b,c)
elif(abs(c-n)>=abs(b-n)):
    print(b)
else:
    print(c)
    