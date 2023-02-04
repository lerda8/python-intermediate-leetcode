class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        s = str(x)
        m = reversed(s)
        if m == s:
            return False
        else:
            return True



s = Solution()
print(s.isPalindrome(1111))