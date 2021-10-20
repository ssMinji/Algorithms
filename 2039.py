def solution(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if sum(nums) - nums[i] - nums[j] == 100:
                return nums[0:i] + nums[i+1:j] + nums[j+1::]
            
            
nums = []
for i in range(9):
    n = int(input())
    nums.append(n)
result = solution(nums)
result.sort()
for r in result:
    print(r)