class Solution:
    def threeSum(nums):
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        return [nums[i], nums[j], nums[k]]
        
list = [-1,0,1,2,-1,-4]
print(Solution.threeSum(list))