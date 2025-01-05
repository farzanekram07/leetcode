# using two loops
def remove1(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1):
            if nums[i] == nums[j]:
                nums.remove(nums[j])             
    return nums

nums = [1, 1, 2]
print(remove1(nums))

# using single loop + extra space
def remove2(nums):
    arr = []
    for i in nums:
        if i not in arr:
            arr.append(i)
    return arr

nums = [1, 1, 2]
print(remove2(nums))

# using hashset()
def remove3(nums):
    hashset = set()
    uniqueValue = []
    for i in nums:
        if i not in hashset:
            hashset.add(i)
            uniqueValue.append(i)
    return uniqueValue

nums = [1, 1, 2]
print(remove3(nums))

# in-place solution
def remove4(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return nums[ :i+1]

nums = [1, 1, 2]
print(remove4(nums))