"""
Problem: Ransom Note

Platform: LeetCode

Difficulty: Easy

Approach:

Use two dictionaries to store the frequency of each character in
`ransomNote` and `magazine`.

1. Create dictionary `d` to count characters in `ransomNote`.
2. Create dictionary `k` to count characters in `magazine`.
3. Traverse every character required by `ransomNote`.
4. Compare its required frequency with the available frequency in
   `magazine`.
5. If the magazine contains fewer occurrences of any required
   character, return `False`.
6. If all required character frequencies are available, return `True`.

Key Idea:

Count the required characters → count the available characters →
make sure the magazine has enough of every required character.

Example:

ransomNote = "aa"
magazine = "aab"

Frequencies:
    ransomNote → a: 2
    magazine   → a: 2, b: 1

The magazine contains enough `a` characters, so the result is `True`.

Time Complexity: O(n + m)

Where:
    n = length of `ransomNote`
    m = length of `magazine`

Space Complexity: O(n + m)

Two dictionaries are used to store character frequencies.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        k = {}

        for ch in ransomNote:
            d[ch] = d.get(ch, 0) + 1
        
        for ch in magazine:
            k[ch] = k.get(ch, 0) + 1

        for key in d.keys():
            if d[key] > k.get(key, 0):
                return False
        
        return True