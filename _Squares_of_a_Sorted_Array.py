n=int(input())
nums=list(map(int,input().split()))
for i in range(len(nums)):
    nums[i] = nums[i] ** 2
nums.sort()
print(*nums)



