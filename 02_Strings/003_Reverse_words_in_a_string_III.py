"""
Problem: Reverse Words in a String III

Platform: LeetCode

Difficulty: Easy

Approach:

1. Split the given string into individual words using `split()`.
2. Traverse each word in the list.
3. Reverse each word using Python slicing `[::-1]`.
4. Join all the reversed words back together using a single space.
5. Return the resulting string.

Key Idea:

Split the sentence into words → reverse each word individually →
join the words back together.

The order of the words remains unchanged; only the characters inside
each word are reversed.

Time Complexity: O(n)

Space Complexity: O(n)

The list of words and the resulting string require O(n) additional space.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()

        for i in range(len(l)):
            l[i] = l[i][::-1]

        s = " ".join(l)

        return s