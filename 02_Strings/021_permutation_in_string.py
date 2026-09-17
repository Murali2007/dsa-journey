"""
Problem: Permutation in String

Platform: LeetCode

Difficulty: Medium

Approach:

Use a fixed-size sliding window and `Counter` to compare character
frequencies.

1. Find the lengths of `s1` and `s2`.
2. Create `target` containing the character frequencies of `s1`.
3. Create a window containing the first `m` characters of `s2`.
4. Compare the frequency of the current window with `target`.
5. Move the window one position at a time:
   - Add the new character entering from the right.
   - Remove the character leaving from the left.
6. Delete a character from the Counter when its frequency becomes zero.
7. If the window's frequency matches `target`, return `True`.
8. If no matching window is found, return `False`.

Key Idea:

Maintain a window of the same length as `s1` and compare its character
frequencies with the frequency of `s1`.

Time Complexity: O(n)

Space Complexity: O(k)

Where `k` is the number of distinct characters stored in the Counters.
"""

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)

        target = Counter(s1)
        window = Counter(s2[:m])

        if target == window:
            return True

        for right in range(m, n):
            window[s2[right]] += 1

            left = right - m

            window[s2[left]] -= 1

            if window[s2[left]] == 0:
                del window[s2[left]]

            if target == window:
                return True

        return False