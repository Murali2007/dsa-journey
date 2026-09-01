"""
Problem: Sort Characters By Frequency

Platform: LeetCode

Difficulty: Medium

Approach:

Use a dictionary to count the frequency of every character in the string.
Traverse the string and increment the frequency of each character.

Then sort the dictionary items based on their frequencies in descending order.
Traverse the sorted characters and append each character multiplied by its
frequency to the result string. This places the most frequent characters first
and continues in decreasing order of frequency.

Time Complexity: O(n + m log m)

Space Complexity: O(n)

where `n` is the length of the string and `m` is the number of distinct
characters.
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        s1 = ""

        for ch in s:
            d[ch] = d.get(ch, 0) + 1

        for ch, num in sorted(d.items(), key=lambda x: x[1], reverse=True):
            s1 += ch * num

        return s1