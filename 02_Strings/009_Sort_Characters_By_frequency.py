"""
Problem: Sort Characters By Frequency

Platform: LeetCode

Difficulty: Medium

Approach:

Use a dictionary to count the frequency of each character and then
sort the characters based on their frequencies.

1. Create an empty dictionary `d`.
2. Traverse the string and store the frequency of each character.
3. Use `sorted()` on the dictionary items.
4. Sort the characters based on their frequency in descending order
   using `key=lambda x: x[1]`.
5. For each character, multiply it by its frequency and append it
   to the result string.
6. Return the resulting string.

Key Idea:

Count each character → sort characters by frequency in descending
order → repeat each character according to its frequency.

Example:

s = "tree"

Frequency:
    t → 1
    r → 1
    e → 2

After sorting by frequency:
    e → 2
    t/r → 1

Possible result:
    "eert"

Time Complexity: O(n + k log k)

Where:
    n = length of the string
    k = number of distinct characters

Space Complexity: O(n)

The dictionary and resulting string require additional space.
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        s1 = ""

        for ch in s:
            d[ch] = d.get(ch, 0) + 1

        for ch, num in sorted(
            d.items(),
            key=lambda x: x[1],
            reverse=True
        ):
            s1 += ch * num

        return s1