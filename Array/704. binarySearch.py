# Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = low + (high - low) // 2  # Avoid overflow
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1  
        else:
            high = mid - 1 
    return -1
  
arr = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found.")



# GFG - Sorted Array Search
# value search 
def linearSearch(nums, k):
    if k in nums:
        return True
    return False
nums = [1, 2, 3, 4, 5, 6]
k = int(input())
print(linearSearch(nums, k))

# index search
def linearSearch(nums, k):
    for i in range(len(nums)):
        if nums[i] == k:
            return i
nums = [-1, 0, 3, 5, 9, 12]
k = int(input())
print(linearSearch(nums, k))        
