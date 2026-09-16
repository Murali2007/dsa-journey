"""
Problem: Longest Substring Without Repeating Characters

Platform: LeetCode

Difficulty: Medium

Approach:

Use the sliding window technique with a set.

1. Maintain a window using `left` and `right` pointers.
2. Store the characters currently present in the window using a set.
3. If `s[right]` is not in the set, add it and expand the window.
4. Update the maximum length whenever a new character is added.
5. If `s[right]` is already in the set, remove characters from the
   left until the duplicate character is removed.
6. Continue expanding the window and return the maximum length found.

Key Idea:

Maintain a window containing only unique characters.
Expand the window when the character is new and shrink it from the
left when a duplicate is found.

Time Complexity: O(n)

Space Complexity: O(n)

The set can contain up to `n` characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k = set()
        left = 0
        right = 0
        res = 0

        while right < len(s):
            if s[right] not in k:
                k.add(s[right])
                right += 1
                res = max(res, len(k))
            else:
                while s[right] in k:
                    k.remove(s[left])
                    left += 1

        return res