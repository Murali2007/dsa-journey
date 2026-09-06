"""
Problem: To Lower Case

Platform: LeetCode

Difficulty: Easy

Approach:

Use Python's built-in `lower()` method to convert all uppercase
characters in the string to lowercase.

1. Take the input string `s`.
2. Call `s.lower()`.
3. Return the resulting lowercase string.

Key Idea:

Use the built-in `lower()` method to convert the entire string
to lowercase.

Time Complexity: O(n)

Space Complexity: O(n)

A new lowercase string is created because Python strings are immutable.
"""

class Solution(object):
    def toLowerCase(self, s):
        return s.lower()