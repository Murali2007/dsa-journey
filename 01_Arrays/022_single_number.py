"""
Problem: Single Number

Platform: LeetCode

Difficulty: Easy

Approach:

Use the bitwise XOR operation to identify the element that appears only once.
Traverse the array and XOR each element with the running result. Since XOR of
two identical numbers is zero and XOR of zero with any number is the number
itself, all duplicate elements cancel each other out. After processing the
entire array, the remaining value is the element that appears exactly once.

Time Complexity: O(n)

Space Complexity: O(1)
"""
class Solution(object):
    def singleNumber(self, nums):
        res = 0

        for i in range(len(nums)):
            res = res ^ nums[i]

        return res