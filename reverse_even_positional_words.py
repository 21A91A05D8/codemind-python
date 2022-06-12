def rev(s):
    return s[::-1]
a=input()
arr=list(a.split())
for i in range(len(arr)):
    if i%2==0:
        print(rev(arr[i]),end=' ')
    else:
        print(arr[i],end=' ')