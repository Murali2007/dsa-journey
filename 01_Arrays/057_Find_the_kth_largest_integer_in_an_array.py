"""
Problem: Kth Largest Integer in an Array

Platform: LeetCode

Difficulty: Medium

Approach:

Convert all numeric strings into integers so that they can be compared based
on their actual numerical values rather than their lexicographical order.
Sort the integers in descending order. The kth largest element will then be at
index `k - 1`. Convert that element back to a string before returning it.

Time Complexity: O(n log n)

Space Complexity: O(n)

where `n` is the number of elements in `nums`.
"""

class Solution:
    def kthLargestNumber(self, nums, k: int) -> str:
        nums = list(map(int, nums))
        nums.sort(reverse=True)

        return str(nums[k - 1])