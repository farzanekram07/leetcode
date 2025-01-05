# Brute Force
def move(list):

    # for i in list:
    #     if i != 0:
    #         nonZeroValue.append(i)
    nonZeroValue = [i for i in list if i != 0]
    zeroCount = len(list) - len(nonZeroValue)
    result = nonZeroValue + [0] * zeroCount
    list[:] = result
    return list

list = [1, 2, 0, 1, 0, 0, 0, 1, 1]
print(move(list))



# Two Pointer Approach
def moveZeroes(list):

    pos = 0
    for i in range(len(list)):
        if list[i] != 0:
            list[pos], list[i] = list[i], list[pos]
            pos += 1
    return list

list = [1, 2, 0, 0, 1, 0, 1]
print(moveZeroes(list))