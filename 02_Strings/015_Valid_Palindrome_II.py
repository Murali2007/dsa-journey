"""
Problem: Valid Palindrome II

Platform: LeetCode

Difficulty: Easy

Approach:

Use two pointers, one from the beginning and one from the end.

1. Compare characters at both pointers.
2. If they match, move both pointers inward.
3. If they do not match, try removing either the left or right character.
4. Check both possibilities using the `isPalindrome()` helper.
5. Return True if either possibility is a palindrome.
6. If no mismatch is found, return True.

Key Idea:

Find the first mismatch and check whether removing either character
makes the string a palindrome.

Time Complexity: O(n)

Space Complexity: O(n)

String slicing creates new strings when checking the two possibilities.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return self.isPalindrome(s[l:r]) or self.isPalindrome(s[l+1:r+1])

            l += 1
            r -= 1

        return True

    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True