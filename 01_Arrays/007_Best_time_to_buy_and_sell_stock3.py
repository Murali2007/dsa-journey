"""```text id="x7q2nv"
Problem: Best Time to Buy and Sell Stock III

Platform: LeetCode

Difficulty: Hard

Approach:

Maintain four variables to represent the best states after each transaction: first buy,
first sell, second buy, and second sell. Update these states while traversing the array,
ensuring that each state stores the maximum profit achievable up to that point. This dynamic
programming approach efficiently computes the maximum profit with at most two transactions in
a single pass.

Time Complexity: O(n)

Space Complexity: O(1)
```
"""
class Solution(object):
    def maxProfit(self, arr):
        buy1 = float('-inf')
        sell1 = 0
        buy2 = float('-inf')
        sell2 = 0

        for price in arr:
            buy1 = max(buy1,-price)
            sell1 = max(sell1,buy1+price)
            buy2 = max(buy2,sell1 - price)
            sell2 = max(sell2,buy2+price)
        
        return sell2