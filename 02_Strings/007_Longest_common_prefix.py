"""
Problem: Longest Common Prefix

Platform: LeetCode

Difficulty: Easy

Approach:

1. Take the first string as the reference string.
2. Traverse each character of the first string using index `i`.
3. For every character, compare it with the character at the same index
   in every other string.
4. If another string ends at the current index, the common prefix ends
   there.
5. If any character does not match the corresponding character in the
   first string, return the prefix found so far.
6. If all characters match, return the entire first string.

Key Idea:

Use the first string as a reference and compare its characters with
the same-position characters of all other strings.

Time Complexity: O(n × m)

Where:
    n = number of strings
    m = length of the first string

Space Complexity: O(1)

Only a few variables are used, excluding the returned substring.
"""

class Solution(object):
    def longestCommonPrefix(self, arr):
        string = arr[0]

        for i in range(len(string)):
            for j in range(1, len(arr)):
                if i == len(arr[j]):
                    return string[:i]

                if arr[j][i] != string[i]:
                    return string[:i]

        return string