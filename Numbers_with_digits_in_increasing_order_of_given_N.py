def printstrictly(n,res="",prev="0"):
    if n==0:
        print(res,end=" ")
        return
    for ch in range(ord(prev)+1,ord('9')+1):
        printstrictly(n-1,res+chr(ch),chr(ch))
n=int(input())
if n==1:
    print("0",end=" ")
printstrictly(n)