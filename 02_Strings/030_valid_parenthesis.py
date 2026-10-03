"""
Problem: Valid Parentheses

Platform: LeetCode

Difficulty: Easy

Approach:

Use a stack to keep track of opening brackets.

1. Traverse every character in the string.
2. If the character is an opening bracket, push it onto the stack.
3. If the character is a closing bracket, check whether the top of the
   stack contains its corresponding opening bracket.
4. If they match, remove the opening bracket from the stack.
5. If they do not match or the stack is empty, return `False`.
6. After processing the entire string, return `True` only if the stack
   is empty.

Key Idea:

The most recently opened bracket must be the first one to be closed,
so a stack follows the required LIFO order.

Time Complexity: O(n)

Space Complexity: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        l = []
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                l.append(ch)
            elif ch == ']':
                if l and l[-1] == '[':
                    l.pop()
                else:
                    return False
            elif ch == '}':
                if l and l[-1] == '{':
                    l.pop()
                else:
                    return False
            elif ch == ')':
                if l and l[-1] == '(':
                    l.pop()
                else:
                    return False

        if l:
            return False
        else:
            return True
        