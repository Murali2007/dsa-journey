"""
Problem: Valid Anagram

Platform: LeetCode

Difficulty: Easy

Approach:

Use two frequency arrays to count the occurrences of every character.

1. Create two arrays of size 1000 initialized with zeros.
2. Traverse string `s` and use `ord(ch)` to convert each character
   into its ASCII/Unicode integer value.
3. Increment the corresponding position in `arr`.
4. Do the same for string `t` using `arr1`.
5. Compare the two frequency arrays.
6. If both arrays are equal, both strings contain the same characters
   with the same frequencies, so they are anagrams.

Key Idea:

Count the frequency of every character in both strings and compare
their frequency arrays.

For example:

s = "anagram"
t = "nagaram"

Both produce the same character frequencies, so the result is `True`.

Time Complexity: O(n + m)

Where:
    n = length of `s`
    m = length of `t`

Space Complexity: O(1)

Two fixed-size arrays of size 1000 are used, so the extra space is
constant with respect to the input size.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 1000
        arr1 = [0] * 1000

        for ch in s:
            arr[ord(ch)] += 1

        for ch in t:
            arr1[ord(ch)] += 1

        return arr == arr1