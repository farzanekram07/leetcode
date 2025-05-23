class Solution:
    def remove_element(nums, val):
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1   
    return nums[:index]
