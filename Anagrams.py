s1=input()
s2=input()
c=0
if len(s1)==len(s2):
    for i in s1:
        if i in s2 or i.upper() in s2 or i.lower() in s2:
            c=1
        else:
            c=0
            break
    if c==1:
        print("True")
    else:
        print("False")
else:
    print("False")
            