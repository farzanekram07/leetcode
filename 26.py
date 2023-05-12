class Solution(object):
        def removeDuplicates(self, nums):
            unique_count = 1
            for i in range(1, len(nums)):
                if nums[i-1] != nums[i]:
                    nums[unique_count] = nums[i]
                    unique_count += 1
            return unique_count