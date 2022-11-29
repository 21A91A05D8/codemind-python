def subsets(nums):
    ans=[[]]
    for j in nums:
        ans+=[i+[j]for i in ans]
    return ans
n=int(input())
l=list(map(int,input().split()))
l=subsets(l)
for i in range(1,len(l)):
    print(*l[i])
#for i in l:
 #   print(*i)