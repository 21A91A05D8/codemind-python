n=input().split()
for i in n:
    vowel=sum(letter in 'aeiou'for letter in i.lower())
    print(vowel,end=' ')