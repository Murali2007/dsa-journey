"""
Problem: Reverse Vowels of a String

Platform: LeetCode

Difficulty: Easy

Approach:

Use two pointers to find vowels from both ends of the string.

1. Store all vowels in a set for quick checking.
2. Convert the string into a list because strings are immutable.
3. Use `l` from the left and `r` from the right.
4. Move `l` forward until it points to a vowel.
5. Move `r` backward until it points to a vowel.
6. Swap the two vowels.
7. Move both pointers inward and continue.
8. Join the list back into a string.

Key Idea:

Find vowels from both ends → swap them → move the pointers inward.

Time Complexity: O(n)

Space Complexity: O(n)

The character list requires O(n) additional space.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] not in vowels:
                l += 1

            if s[r] not in vowels:
                r -= 1
            
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        return "".join(s)