"""
Problem: Max Consecutive Ones
Platform: LeetCode
Difficulty: Easy

Approach:
Traverse the array once, counting consecutive 1s and resetting the count on 0,
while keeping track of the maximum consecutive count encountered

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def ConsecutiveOnes(arr):
        res = 0
        curr = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                curr = 0
            else:
                curr += 1
                res = max(res,curr)

        return res