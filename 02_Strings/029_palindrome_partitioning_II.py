"""
Problem: Palindrome Partitioning II

Platform: LeetCode

Difficulty: Hard

Approach:

Use dynamic programming with palindrome preprocessing.

1. Create a `pal` table where `pal[i][j]` indicates whether the substring
   from index `i` to `j` is a palindrome.
2. Fill the table from right to left so that smaller palindrome results
   are available when checking larger substrings.
3. Create `dp`, where `dp[i]` stores the minimum number of palindrome
   partitions needed for the suffix starting at index `i`.
4. Use DFS with memoization to try every palindromic substring starting
   at index `i`.
5. For every valid palindrome `s[i:j+1]`, recursively solve the remaining
   suffix.
6. Store the minimum number of partitions in `dp[i]`.
7. The DFS counts partitions, so subtract `1` to convert the number of
   partitions into the number of cuts.

Key Idea:

Precompute which substrings are palindromes, then use DP to find the
minimum number of palindrome partitions.

Time Complexity: O(n²)

Space Complexity: O(n²)

The palindrome table requires O(n²) space, while the DP array and
recursion use O(n) additional space.
"""

class Solution:
    def minCut(self, s: str) -> int:

        def dfs(i,dp,pal):
            min_cost = float('inf')
            if i == len(s):
                return 0

            if dp[i] != -1:
                return dp[i]

            for j in range(i,len(s)):
                if pal[i][j]:
                    c = 1 + dfs(j+1,dp,pal)
                    min_cost = min(c,min_cost)
            
            dp[i] = min_cost
            return dp[i]

        dp = [-1] * len(s)
        n = len(s)
        pal = [[False] * n for i in range(n)]
        
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i] == s[j] and (j - i <= 2 or pal[i+1][j-1]):
                    pal[i][j] = True

        return dfs(0,dp,pal) - 1
        
                
    def ispalin(self,s,i,j):
        while(i < j):
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

        