"""
Problem: Two Sum
Platform: LeetCode
Difficulty: Easy

Approach:
Use a hash map to store visited numbers.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in seen:
                return [seen[diff], i]

            seen[num] = i