class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashset = {}
        n = len(nums)


        for i in range(n):
            diff = target - nums[i]
            if diff in hashset:
                return [hashset[diff], i]
            hashset[nums[i]] = i


        return []