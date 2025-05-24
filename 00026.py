# brute force - O(n2)|O(n)
def remove_duplicates(nums):
    result = []
    for i in nums:
        if i not in result:
            result.append(i)
    return result 

# hashmap - O(n)|O(n)
def remove_duplicates1(nums):
    result = set()
    for i in nums:
        result.add(i)
    return list(result)

# two-pointer -> in-place - O(n)|O(1) 
def remove_duplicates2(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return nums[:i+1]
