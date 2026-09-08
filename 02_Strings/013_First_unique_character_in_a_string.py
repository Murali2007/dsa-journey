"""
Problem: First Unique Character in a String

Platform: LeetCode

Difficulty: Easy

Approach:

Use a dictionary to count the frequency of every character.

1. Traverse the string and store the frequency of each character
   in dictionary `d`.
2. Traverse the dictionary in insertion order.
3. Find the first character whose frequency is exactly 1.
4. Use `s.index(key)` to find the index of that unique character.
5. If no character occurs exactly once, return -1.

Key Idea:

Count the frequency of each character → find the first character
with frequency 1 → return its index.

Example:

s = "leetcode"

Frequencies:
    l → 1
    e → 3
    t → 1
    c → 1
    o → 1
    d → 1

The first unique character is `l`, so return index `0`.

Time Complexity: O(n)

Space Complexity: O(n)

The dictionary stores the frequency of the characters.

"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}

        for ch in s:
            d[ch] = d.get(ch, 0) + 1
        
        for key, val in d.items():
            if val == 1:
                return s.index(key)

        return -1