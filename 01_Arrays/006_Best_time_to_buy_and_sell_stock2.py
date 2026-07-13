"""```text
Problem: Best Time to Buy and Sell Stock II

Platform: LeetCode

Difficulty: Medium

Approach:

Traverse the array and add every positive price difference between consecutive days to the
total profit. This greedy approach captures the maximum possible profit by taking advantage
of every increasing price sequence, allowing multiple buy and sell transactions.

Time Complexity: O(n)

Space Complexity: O(1)
```
"""

class Solution(object):
    def maxProfit(self, arr):
        profit = 0
        for i in range(1,len(arr)):
            if arr[i] > arr[i-1]:
                profit = profit + (arr[i] - arr[i-1])
        
        return profit