s=input()
c=0
for i in s:
    if s.count(i)==1:
        print(i)
        quit()
print("-1")