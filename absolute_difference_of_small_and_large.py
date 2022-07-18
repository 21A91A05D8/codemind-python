n=input().split()
for i in n:
    print(abs(ord(max(i)))-ord(min(i)),end=' ')