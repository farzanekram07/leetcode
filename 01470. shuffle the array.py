from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left = 0
        right = n
        newArr = []
        while right < len(nums):
            newArr.append(nums[left])
            newArr.append(nums[right])
            left += 1
            right += 1
        return newArr
    
nums = [2,5,1,3,4,7]; n = 3
print(Solution().shuffle(nums, n))