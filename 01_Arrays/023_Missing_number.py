"""
Problem: Missing Number

Platform: LeetCode

Difficulty: Easy

Approach:

Iterate through all numbers from 0 to n, where n is the length of the array.
For each number, check whether it exists in the array. The first number that is
not found is the missing number, so return it immediately. Since each membership
check scans the array, the process is repeated for every possible number until
the missing value is identified.

Time Complexity: O(n²)

Space Complexity: O(1)
"""
class Solution(object):
    def missingNumber(self, nums):
        for i in range(len(nums) + 1):
            if i not in nums:
                return i