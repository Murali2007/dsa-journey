"""
Problem: Palindromic Substrings

Platform: LeetCode

Difficulty: Medium

Approach:

Use the expand-around-center technique to count all palindromic substrings.

1. Treat each character as the center of an odd-length palindrome.
2. Expand `l` and `r` outward while the characters are equal.
3. Increment `count` for every valid palindrome found.
4. Treat the gap between the current character and the next character as
   the center of an even-length palindrome.
5. Expand outward again and count every valid palindrome.
6. Repeat for every position in the string.
7. Return the total count.

Key Idea:

Every palindrome can be found by expanding around its center.
Check both odd-length and even-length centers.

Time Complexity: O(n²)

Space Complexity: O(1)
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            l = i
            r = i
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                count += 1
                l -= 1
                r += 1
            
            l = i
            r = i+1
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                count += 1
                l -= 1
                r += 1
            
        return count
               
    
    

        