s=input()
v='AEIOUaeiou'
vo=0
co='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
c=0
d=0
ws=0
w=' '
for i in s:
    if i in v:
        vo+=1
    if i in co:
        c+=1
    if i.isdigit():
        d+=1
    if i in w:
        ws+=1
print("Vowels:",vo)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",ws)