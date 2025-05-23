# brute force
def remove_element0(nums, val):
    result = []
    for i in nums:
        if i != val:
            result.append(i)
    return result

# optimization - using two pointer
def remove_element1(nums, val):
    start = 0
    for i, num in enumerate(nums):
        if num == val:
            continue
        else:
            nums[start] = nums[i]
            start += 1
    return nums[:start]

def remove_element2(nums, val):
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1   
    return nums[:index]
