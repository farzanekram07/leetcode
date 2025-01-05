# # using slicing method
# def rotateArray1(nums, k):
#     return nums[k+1:] + nums[:k+1]

# k = 3
# nums = [1, 2, 3, 4, 5, 6, 7]
# print(rotateArray1(nums, k))

# # Brute Force
# def rotateArray2(nums, k):
#     n = len(nums)
#     k = k % n   # handle case if k > n
#     for _ in range(k):
#         last = nums[-1]
#         for i in range(n-1, 0, -1):
#             nums[i] = nums[i -1]
#         nums[0] = last
#     return nums

# k = 2
# nums = [1, 2, 3, 4, 5]
# print(rotateArray2(nums, k))




def rotate(nums, k):
    n = len(nums)
    k = k % n

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    reverse(0, n-1)
    reverse(0, k-1)
    reverse(k, n-1)

nums = [1, 2, 3, 4, 5]
k = 2
rotate(nums,k)
print(nums)



