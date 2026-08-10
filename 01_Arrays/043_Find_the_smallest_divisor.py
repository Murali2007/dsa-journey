"""
Problem: Find the Smallest Divisor Given a Threshold

Platform: LeetCode

Difficulty: Medium

Approach:

Use Binary Search on the possible divisor values. The minimum possible divisor
is 1 and the maximum possible divisor is the largest element in the array. For
each candidate divisor, calculate the sum of the ceiling values obtained by
dividing every number by the divisor. If this sum is less than or equal to the
given threshold, the divisor is sufficient, so search for a smaller divisor by
moving the high pointer to `mid`. Otherwise, the divisor is too small, so move
the low pointer to `mid + 1`. When both pointers converge, `low` represents the
smallest divisor that satisfies the threshold.

Time Complexity: O(n log(max(nums)))

Space Complexity: O(1)
"""
import math

class Solution(object):
    def smallestDivisor(self, nums, threshold):
        low = 1
        high = max(nums)

        while low < high:
            mid = (low + high) // 2

            s = 0
            for i in range(len(nums)):
                s += math.ceil(float(nums[i]) / mid)

            if s <= threshold:
                high = mid
            else:
                low = mid + 1

        return low