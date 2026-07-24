"""
Problem: First Missing Positive

Platform: LeetCode

Difficulty: Hard

Approach:

Use the Cyclic Sort technique to place every positive integer in the range
1 to n at its correct index, where the value x should be placed at index x - 1.
Traverse the array and repeatedly swap each valid positive number with the
element at its correct position until every possible number is correctly placed.
After the rearrangement, scan the array from left to right. The first index
where the value does not equal index + 1 indicates the smallest missing positive
integer. If every position contains the correct value, then the answer is n + 1.

Time Complexity: O(n)

Space Complexity: O(1)
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        i = 0

        while i < n:
            correct = nums[i] - 1

            if (1 <= nums[i] <= n) and (nums[i] != nums[correct]):
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1