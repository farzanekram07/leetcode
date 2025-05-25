def majority_element0(nums):
        result = [0] * (max(nums) + 1)
        for i in nums:
            result[i] += 1
        max_count = max(result)
        return result.index(max_count)

# leetcode and neetcode
def majority_element1(nums):
        dict = {}
        for num in nums:
               dict[num] = dict.get(num, 0) + 1
        return max(dict, key=dict.get)


# handle edge case - like gfg 
def majority_element2(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    n = len(nums)
    for num in count:
        if count[num] > n // 2:
            return num
    
    return None  # or raise an Excep