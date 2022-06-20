n=int(input())
td=len(str(n))
sq=n**2
ld=sq%pow(10,td)
if n==ld:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")