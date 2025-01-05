# Merge two sorted arrays - inplace


# Merge two sorted arrays ignoring zeroes in new List DS
def mergeSortedArray(arr1, arr2):
    i, j = 0, 0
    newList = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == 0:
            i += 1
            continue
        elif arr2[j] == 0:
            j += 1
            continue

        elif arr1[i] < arr2[j]:
            newList.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            newList.append(arr2[j])
            j += 1
        else:
            newList.append(arr1[i])
            newList.append(arr2[j])
            i += 1
            j += 1
    while i < len(arr1):
        # if arr1[i] == 0:
        #     i += 1
        #     continue
        # newList.append(arr1[i])
        if arr1[i] != 0:
            newList.append(arr1[i])
        i += 1
    while j < len(arr2):
        # if arr2[j] == 0:
        #     j += 1
        #     continue
        # newList.append(arr2[j])
        if arr2[j] != 0:
            newList.append(arr2[j])
        j += 1
    return newList

arr1 = [1, 2, 3, 0, 0, 0]
arr2 = [2, 5, 0, 6, 0]
print(mergeSortedArray(arr1, arr2))