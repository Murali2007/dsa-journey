"""
Problem: Remove Duplicate Letters

Platform: LeetCode

Difficulty: Medium

Approach:

Use a greedy strategy with a stack.

1. Store the last occurrence of every character in `last`.
2. Traverse the string from left to right.
3. Use `k` to keep track of characters already present in the stack.
4. If the current character is already in the stack, skip it.
5. While the top character of the stack is greater than the current
   character and appears again later, remove it from the stack.
6. Add the current character to the stack and mark it as used.
7. Join the stack to obtain the smallest lexicographical result containing
   every distinct character exactly once.

Key Idea:

Remove a larger character from the stack only when it appears again later,
so a smaller character can be placed before it without losing any required
character.

Time Complexity: O(n)

Space Complexity: O(n)
"""
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {}

        for i in range(len(s)):
            last[s[i]] = i

        stack = []
        k = set()

        for i in range(len(s)):
            ch = s[i]
            if ch in k:
                continue

            while stack and stack[-1] > ch and last[stack[-1]] > i:
                m = stack.pop()
                k.remove(m)

            stack.append(ch)
            k.add(ch)

        return ''.join(stack)
        