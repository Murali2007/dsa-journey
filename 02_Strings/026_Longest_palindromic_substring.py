"""
Problem: Longest Palindromic Substring

Platform: LeetCode

Difficulty: Medium

Approach:

Use the expand-around-center technique.

1. Treat each character as the center of an odd-length palindrome.
2. Expand `left` and `right` outward while the characters are equal.
3. Store the longest palindrome found.
4. Check adjacent equal characters as the center of an even-length palindrome.
5. Expand outward in the same way for the even-length case.
6. Update `res` whenever a longer palindrome is found.
7. Return the longest palindromic substring.

Key Idea:

Every palindrome has a center. Expand outward from each possible center
and keep the longest palindrome found.

Time Complexity: O(n²)

Space Complexity: O(n)

The algorithm uses O(1) auxiliary space, but string concatenation creates
new strings during expansion.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            left = i-1
            right = i+1
            s1 = s[i]
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                s1 = s[left] + s1 + s[right]
                left -= 1
                right += 1

            if len(s1) > len(res):
                res = s1
                

            if i < len(s)-1 and s[i] == s[i+1]:
                s1 = s[i]+s[i+1]
                left = i-1
                right = i+2

                while(left >= 0 and right < len(s) and s[left] == s[right]):
                    s1 = s[left] + s1 + s[right]
                    left -= 1
                    right += 1

            
                if len(s1) > len(res):
                    res = s1

        return res






   

            
        