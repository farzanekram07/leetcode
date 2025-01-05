import re 

class Solution():
    def isPalindrome(s):
        newStr =  re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(newStr)
        left = 0
        right = len(newStr)-1
        while left < right:
            if newStr[left] == newStr[right]:
                left += 1
                right -= 1
            else:
                return False
        return True 
string = "A man, a plan, a canal: Panama"
print(Solution.isPalindrome(string))