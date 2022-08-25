s = input().split(" ")
c=0
v="AEIOUaeiou"
co="QWRTYPLKJHGFDSZXCVBNMqwrtyplkjhgfdszxcvbnm"
for i in s:
    x=0
    y=len(i)-1
    while(x<y):
        if((i[x] in v and i[y] in co) or (i[x] in co and i[y] in v)):
            c+=1
        x+=1
        y-=1
print(c)