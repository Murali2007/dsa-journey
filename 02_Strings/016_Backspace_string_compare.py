"""
Problem: Backspace String Compare

Platform: LeetCode

Difficulty: Easy

Approach:

Use a stack to process each string.

1. Traverse each character of the string.
2. If the character is `#`, remove the last character from the stack
   if the stack is not empty.
3. Otherwise, add the character to the stack.
4. Process both strings using the same method.
5. Compare the two resulting stacks.

Key Idea:

Use a stack where normal characters are pushed and `#` removes the
most recently added character.

Time Complexity: O(n + m)

Space Complexity: O(n + m)

The stacks store the processed characters of both strings.
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.createStack(s) == self.createStack(t)
        
    def createStack(self, s):
        stack = []

        for ch in s:
            if ch == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)

        return stack