"""
Problem: Reverse String

Platform: LeetCode

Difficulty: Easy

Approach:

Use the two-pointer technique.

1. Set `i` at the beginning of the array and `j` at the end.
2. Swap the characters at positions `i` and `j`.
3. Move `i` forward and `j` backward.
4. Continue until the two pointers meet or cross.
5. The array is reversed in-place.

Key Idea:

Use two pointers from both ends and swap the characters while moving
towards the center.

Time Complexity: O(n)

Space Complexity: O(1)

The string is reversed in-place without using an additional array.
"""

class Solution:
    def reverseString(self, s) -> None:
        i = 0
        j = len(s) - 1

        while i <= j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return s