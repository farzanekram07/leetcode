# Two Pointer
def twoSum(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        currentSum = nums[left] + nums[right]
        if currentSum == target:
            return[left, right]
        elif currentSum < target:
            left += 1
        else:
            right -= 1
    return [left, right]

nums = [1, 2, 17, 4, 5, -6]
target = 11
print(twoSum(nums, target))



# Optimized - Hashset
class Solution:
    def twoSum(self, nums, target):
        
        hashset = {}
        n = len(nums)


        for i in range(n):
            diff = target - nums[i]
            if diff in hashset:
                return [hashset[diff], i]
            hashset[nums[i]] = i


        return []