n=int(input())
a=map(int,input().split())
b=map(int,input().split())
s1=sum(a)
s2=sum(b)
if(abs(s1-s2>0)):
    print('0')
else:
    print(abs(s1-s2))