class Solution(object):
    def isPalindrome(self, s):
        k = ""
        for ch in s:
            if ch.isalnum():
                k += ch.lower()
        
        return k == k[::-1]