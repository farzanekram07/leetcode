class Solution:
    def buildArray(nums):
        for i in nums:
            return [nums[nums[i]]]
        i += 1

nums = list(map(int, input().split()))
print(Solution.buildArray(nums))