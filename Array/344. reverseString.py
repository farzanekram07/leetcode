class Solution():
    #1. using return function
    def reverseString(s):
        return s[::-1]

    #2. in-place reversing
    def reverseString1(s):
        
        low, high = 0, len(s)-1
        while low < high:
             s[low], s[high] = s[high], s[low]
             low += 1
             high -= 1
        print(s)

string = ["h","e","l","l","o"]
print(Solution.reverseString(string))
Solution.reverseString1(string)