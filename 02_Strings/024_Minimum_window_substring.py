"""
Problem: Minimum Window Substring

Platform: LeetCode

Difficulty: Hard

Approach:

Use the sliding window technique with two pointers.

1. Store the required frequency of each character in `t` using a Counter.
2. Maintain another Counter for character frequencies inside the current window.
3. Use `have` to track how many required characters currently satisfy their
   required frequency.
4. Expand the window using `i` and add each character to the window.
5. When the current window satisfies all required character frequencies,
   shrink the window from the left using `j`.
6. Before shrinking, update the minimum window if the current window is smaller.
7. When removing a character causes a required frequency to become
   unsatisfied, decrease `have`.
8. Return the smallest valid window.

Key Idea:

A window is valid when all characters of `t` are present with their
required frequencies.

Time Complexity: O(n + m)

Space Complexity: O(n + m)
"""

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        window = Counter()
        need = Counter(t)
        have = 0
        
        j = 0
        min_length = float('inf')
        need_count = len(need)
        res = ""

        for i in range(len(s)):
            ch = s[i]
            window[ch] += 1

            if ch in need and window[ch] == need[ch]:
                have += 1
            
            while have == need_count:
                length = i - j + 1

                if length < min_length:
                    min_length = length
                    res = s[j:i+1]
                
                left_ch = s[j]

                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1
                
                j += 1

        return res