from typing import List

# solution 1
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        min_val = min(nums)
        max_val = max(nums)

        range_of_elements = max_val - min_val + 1
        count = [0] * range_of_elements

        for num in nums:
            count[num - min_val] += 1

        sorted_arr = []
        for num, freq in enumerate(count):
            sorted_arr.extend([num + min_val] * count[num])
            # sorted_arr.extend([num + min_val] * freq)
        return sorted_arr
    

# solution 2
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)
    