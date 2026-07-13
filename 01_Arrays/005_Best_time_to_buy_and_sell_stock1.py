"""
Problem: Best Time to Buy and Sell Stock

Platform: LeetCode

Difficulty: Easy

Approach:

Traverse the array while keeping track of the minimum stock price seen so far. At each step,
calculate the profit by selling on the current day and update the maximum profit if it is
greater than the previous maximum. This ensures the optimal buy and sell prices are found in
a single pass.

Time Complexity: O(n)

Space Complexity: O(1)
```
"""

class Solution(object):
    def maxProfit(self, arr):
        min_value = arr[0]
        max_profit = 0
        for i in range(1,len(arr)):
            min_value = min(min_value,arr[i])
            profit = arr[i] - min_value
            max_profit = max(max_profit,profit)
        
        return max_profit