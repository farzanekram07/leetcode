# leetcode solution
def longestSubstring(s):
    left = maxlength = 0
    charset = set()

    for right in range(len(s)):
        while s[right] in charset:
            charset.remove(s[left])
            left += 1
        charset.add(s[right])
        maxlength = max(maxlength, right - left + 1)
    return maxlength

string = "abcabcaa"
print(longestSubstring(string))



# brute force 
def longestSubstring(arr, k):
    maxtotal = 0

    for i in range(len(arr)-k+1):
        total = sum(arr[i:i+k])
        maxtotal = max(maxtotal, total)
    return arr[i:], maxtotal

arr = [3, 5, 1, 4, 8]
print(longestSubstring(arr, k=3))



# sliding window
def longestSubstringSum(arr, k):
    #handle the case where len(n) < k
    if len(arr) < k:
        return -1
    windowSum = sum(arr[:k])
    maxtotal = windowSum

    for i in range(len(arr)-k):
        windowSum = windowSum - arr[i]
        windowSum = windowSum + arr[i+k]
        maxtotal = max(maxtotal, windowSum)

    return maxtotal, arr[i+1:]

arr = [3, 5, 1, 4, 8]
print(longestSubstringSum(arr, k=3))