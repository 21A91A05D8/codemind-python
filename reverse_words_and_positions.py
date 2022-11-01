s=input().split()
c=(reversed(s))
s=[]
for i in c:
   s.append(i[::-1]) 
print(" ".join(s))