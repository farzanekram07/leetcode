## here we don't care about the actual
## values we just got the longest length


## Dynamic Programming
def naive(arr):
    n = len(arr)
    greater = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                greater[i] = max(greater[i], greater[j] + 1)
    return max(greater), greater
        
arr = [12, 11, 10, 5, 6, 2, 30]
print(naive(arr))



# optimized version - (Patience Sorting / Binary Search method):
import bisect

def lis_optimized(arr):
    sub = []
    for num in arr:
        idx = bisect.bisect_left(sub, num)
        if idx == len(sub):
            sub.append(num)  
        else:
            sub[idx] = num 
    return len(sub)

arr = [12, 11, 10, 5, 6, 2, 30]
print(lis_optimized(arr))



# Let’s walk through how sub evolves:
# num	Action	                    sub
# 12	append (sub is empty)	    [12]
# 11	replace sub[0] (11 < 12)	[11]
# 10	replace sub[0] (10 < 11)	[10]
# 5	    replace sub[0] (5 < 10)	    [5]
# 6	    append (6 > 5)	            [5, 6]
# 2	    replace sub[0] (2 < 5)	    [2, 6]
# 30	append (30 > 6)	            [2, 6, 30]
# 📏 Final Length of sub = 3 → That's the LIS!