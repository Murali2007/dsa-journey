"""
Problem: Isomorphic Strings

Platform: LeetCode

Difficulty: Easy

Approach:

Use a dictionary to maintain the mapping from characters in `s` to
characters in `t`.

1. First check whether both strings have the same length. If not,
   they cannot be isomorphic.
2. Create a dictionary `d` where:
       key   = character from `s`
       value = corresponding character from `t`
3. Traverse both strings using the same index.
4. If the current character from `s` has not been mapped yet:
   - Check whether the current character from `t` is already used as
     a value in the dictionary.
   - If it is already used, return `False`.
   - Otherwise, create the new mapping.
5. If the character from `s` already has a mapping, verify that it
   maps to the current character in `t`.
6. If all characters satisfy the mapping rules, return `True`.

Key Idea:

Maintain a one-to-one mapping between characters of `s` and `t`.

Example:

s = "egg"
t = "add"

Mapping:
    e → a
    g → d

Since the same characters always map to the same characters and
different characters do not map to the same character, the strings
are isomorphic.

Time Complexity: O(n)

Space Complexity: O(n)

The dictionary stores the character mappings. In the worst case,
there can be O(n) distinct characters.

"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = {}

        for i in range(len(s)):
            k = d.get(s[i], 0)

            if k == 0:
                if t[i] in d.values():
                    return False

                d[s[i]] = t[i]
            else:
                if k != t[i]:
                    return False

        return True