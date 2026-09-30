"""
Problem: Palindrome Partitioning

Platform: LeetCode

Difficulty: Medium

Approach:

Use backtracking with DFS to generate all possible palindrome partitions.

1. Start from index `0` and consider every possible substring starting at
   the current index.
2. Check whether the selected substring is a palindrome using `ispalin()`.
3. If it is a palindrome, add it to the current partition.
4. Recursively continue from the next index.
5. When the entire string has been processed, copy the current partition
   into `res`.
6. Remove the last substring using `pop()` to backtrack and try the next
   possible partition.

Key Idea:

At each position, choose every possible palindromic substring and use
backtracking to explore all valid partitions.

Time Complexity: O(n * 2^n)

Space Complexity: O(n)

The recursion depth and current partition require O(n) auxiliary space.
The result itself can require O(n * 2^n) space.
"""
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i,len(s)):
                if self.ispalin(s,i,j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()

        dfs(0)
        return res

    def ispalin(self,s,i,j):
        while(i < j):
            if s[i] != s[j]:
                return False
            i,j = i + 1, j - 1
        return True

        