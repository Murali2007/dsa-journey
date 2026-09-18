"""
Problem: Find All Anagrams in a String

Platform: LeetCode

Difficulty: Medium

Approach:

Use a fixed-size sliding window and `Counter` to compare character
frequencies.

1. Create a `Counter` for the first `n` characters of `s`.
2. Create a `Counter` for the pattern `p`.
3. Compare both Counters. If they are equal, index `0` is an anagram.
4. Move the window one character at a time.
5. Add the new character entering the window.
6. Remove the character leaving the window.
7. Delete a character from the Counter when its frequency becomes zero.
8. If the window frequency matches the target frequency, add the
   starting index of the window to the result.
9. Return all the starting indices.

Key Idea:

Maintain a window of the same length as `p` and compare its character
frequencies with the frequency of `p`.

Time Complexity: O(m + n)

Where:
    m = length of `s`
    n = length of `p`

Space Complexity: O(k)

Where `k` is the number of distinct characters stored in the Counters.
"""

from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        m = len(s)
        n = len(p)
        l = []

        window = Counter(s[:n])
        target = Counter(p)

        if window == target:
            l.append(0)

        for i in range(n, m):
            window[s[i]] += 1

            left = i - n
            window[s[left]] -= 1

            if window[s[left]] == 0:
                del window[s[left]]
            
            if window == target:
                l.append(i - n + 1)
        
        return l