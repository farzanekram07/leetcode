from typing import List

# solution 1
class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        min_value = min(arr)
        max_value = max(arr)

        range_of_number = (max_value - min_value) + 1
        count = [0] * range_of_number

        for num in arr:
            count[num-min_value] += 1

        i = 0
        for num in range(range_of_number):
            for _ in range(count[num]):
                arr[i] = num + min_value
                i += 1

# solution 2
class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(arr) - 1

        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
        return arr