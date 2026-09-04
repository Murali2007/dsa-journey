"""
Problem: Wiggle Sort

Platform: LeetCode

Difficulty: Medium

Approach:

First, sort the array in ascending order. Split the sorted array into two
parts: the smaller half and the larger half. Start from the end of both halves
and alternately take elements from the smaller half and the larger half.

The smaller elements are placed at even positions and the larger elements are
placed at odd positions. Traversing both halves from right to left helps keep
equal values separated as much as possible and produces the required wiggle
pattern:

nums[0] <= nums[1] >= nums[2] <= nums[3] ...

After constructing the result array, copy its elements back into `nums`.

Time Complexity: O(n log n)

Space Complexity: O(n)

The sorting takes O(n log n), and the additional result list requires O(n)
space.
"""
class Solution:
    def wiggleSort(self, nums) -> None:
        nums.sort()
        res = []

        mid = (len(nums) + 1) // 2

        i = mid - 1
        j = len(nums) - 1

        while i >= 0 and j >= mid:
            res.append(nums[i])
            res.append(nums[j])
            i -= 1
            j -= 1

        while i >= 0:
            res.append(nums[i])
            i -= 1

        while j >= 0:
            res.append(nums[j])
            j -= 1

        for i in range(len(nums)):
            nums[i] = res[i]