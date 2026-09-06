"""
Problem: Length of Last Word

Platform: LeetCode

Difficulty: Easy

Approach:

1. Start from the end of the string using a negative index.
2. Skip all trailing whitespace characters using `isspace()`.
3. Once the last word is reached, move backwards while the characters
   are alphabetic using `isalpha()`.
4. Increment `count` for every character in the last word.
5. Return `count`.

Key Idea:

Start from the end → skip trailing spaces → count characters of the
last word until whitespace or the beginning of the string is reached.

Time Complexity: O(n)

Space Complexity: O(1)

The solution uses only a few variables and does not create any
additional array or string.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = -1

        while i >= -len(s) and s[i].isspace():
            i -= 1

        count = 0

        while i >= -len(s) and s[i].isalpha():
            i -= 1
            count += 1

        return count