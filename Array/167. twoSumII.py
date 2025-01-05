# two Sum II
def twoSum(number, target):
    left = 0
    right =  len(number) - 1

    while left < right:
        if number[left] + number[right] == target:
            return [left + 1, right + 1]
        elif number[left] + number[right] > target:
            right -= 1
        else:
            left += 1
    return [-1, -1]


number = [2, 7, 11, 15]
print(twoSum(number, target=9))