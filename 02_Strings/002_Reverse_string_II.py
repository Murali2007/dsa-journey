"""
Problem: Reverse String II

Platform: LeetCode

Difficulty: Easy

Approach:

The string is processed in groups of `k` characters.

1. Reverse the first `k` characters using slicing.
2. Start processing the remaining characters from index `k`.
3. Use `count` to track the number of characters added without reversing.
4. Once `count == k`, reverse the next `k` characters.
5. If fewer than `k` characters remain, reverse all of the remaining
   characters.
6. Continue this process until the entire string is processed.
7. Return the constructed result string.

Key Idea:

For every group of `2k` characters:
    - Reverse the first `k` characters.
    - Keep the next `k` characters unchanged.

The solution constructs the final string using slicing and concatenation.

Time Complexity: O(n)

Space Complexity: O(n)

The result string requires O(n) additional space.
"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = s[k-1::-1]
        i = k
        count = 0

        while i < len(s):
            if count == k:
                if i + k <= len(s):
                    res += s[i+k-1:i-1:-1]
                    i += k
                    count = 0
                    continue
                else:
                    res += s[len(s)-1:i-1:-1]
                    i += k
                    continue

            res += s[i]
            count += 1
            i += 1

        return res