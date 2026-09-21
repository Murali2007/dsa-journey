"""
Problem: Longest Repeating Character Replacement

Platform: LeetCode

Difficulty: Medium

Approach:

Use the sliding window technique with a frequency Counter.

1. Maintain a window using `j` as the left pointer and `i` as the right pointer.
2. Store the frequency of each character in the current window.
3. Calculate the number of replacements needed using:
       window length - maximum character frequency
4. If the required replacements are at most `k`, expand the window.
5. If more than `k` replacements are required, shrink the window from
   the left and update the character frequencies.
6. Keep track of the maximum valid window length.
7. Return the maximum length.

Key Idea:

A window is valid when the number of characters that need to be
replaced is at most `k`.

Replacements needed = window length - most frequent character count.

Time Complexity: O(n)

Space Complexity: O(k)

The Counter stores the frequencies of the characters in the window.
"""

from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = Counter(s[0])
        i = 0
        j = 0
        res = 0

        while i < len(s) and j < len(s):
            length = i - j + 1
            n = length - max(d.values())

            if n <= k:
                res = max(res, length)
                i += 1

                if i < len(s):
                    d[s[i]] += 1
            else:
                d[s[j]] -= 1

                if d[s[j]] == 0:
                    del d[s[j]]

                j += 1

        return res