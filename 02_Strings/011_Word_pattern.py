"""
Problem: Word Pattern

Platform: LeetCode

Difficulty: Easy

Approach:

Use a dictionary to maintain a one-to-one mapping between characters
in `pattern` and words in the string `s`.

1. Split `s` into a list of words using `split()`.
2. Check whether the number of pattern characters is equal to the
   number of words. If not, return `False`.
3. Create a dictionary `d` where:
       key   = character from `pattern`
       value = corresponding word from `s`
4. Traverse the pattern and word list simultaneously.
5. If the current pattern character has not been mapped:
   - Check whether the current word is already used as a dictionary
     value.
   - If it is already used, return `False`.
   - Otherwise, create the new mapping.
6. If the pattern character already has a mapping, check whether it
   maps to the current word.
7. If all mappings are valid, return `True`.

Key Idea:

Maintain a one-to-one mapping between pattern characters and words.

Example:

pattern = "abba"
s = "dog cat cat dog"

Mapping:
    a → dog
    b → cat

The mapping remains consistent, so the result is `True`.

Time Complexity: O(n)

Space Complexity: O(n)

The dictionary and list created by `split()` require additional space.
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l = s.split()

        if len(pattern) != len(l):
            return False
        
        d = {}

        for i in range(len(l)):
            k = d.get(pattern[i], 0)

            if k == 0:
                if l[i] in d.values():
                    return False

                d[pattern[i]] = l[i]
            else:
                if k != l[i]:
                    return False
            
        return True