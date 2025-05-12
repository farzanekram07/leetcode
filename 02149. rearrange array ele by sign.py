# hardcode by its OK
def modifyArr(nums):
    arr = [0] * len(nums)
    i = 0
    j = 1

    for num in nums:
        if num > 0:
            arr[i] = num
            i += 2
        else:
            arr[j] = num
            j += 2

    return arr

arr = [3,1,-2,-5,2,-4]
print(modifyArr(arr))