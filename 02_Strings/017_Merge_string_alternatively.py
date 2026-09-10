"""
Problem: Merge Strings Alternately

Platform: LeetCode

Difficulty: Easy

Approach:

Use two pointers to traverse both strings.

1. Start `i` at the beginning of `word1` and `j` at the beginning of
   `word2`.
2. Add one character from each string alternately to the result.
3. Continue until one of the strings is completely processed.
4. Add the remaining characters from the other string.
5. Return the final merged string.

Key Idea:

Take one character from `word1`, then one from `word2`, and continue
alternately until both strings are processed.

Time Complexity: O(n + m)

Space Complexity: O(n + m)

The result string requires additional space for all characters.
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        s = ""

        while i < len(word1) and j < len(word2):
            s += word1[i]
            i += 1
            s += word2[j]
            j += 1
        
        while i < len(word1):
            s += word1[i]
            i += 1

        while j < len(word2):
            s += word2[j]
            j += 1

        return s