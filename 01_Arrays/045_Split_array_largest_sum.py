"""
Problem: Split Array Largest Sum

Platform: LeetCode

Difficulty: Hard

Approach:

Use Binary Search on the possible value of the largest subarray sum. The
minimum possible value is the largest element in the array because every
subarray must contain its elements, while the maximum possible value is the
sum of the entire array when all elements are placed in one subarray. For each
candidate maximum sum, greedily split the array into subarrays by adding
elements to the current subarray until adding the next element would make its
sum greater than the candidate value. When that happens, start a new subarray.
Count the total number of subarrays formed. If the number of parts is less than
or equal to `k`, the candidate value is sufficient because we can split further
if necessary, so search for a smaller maximum sum. Otherwise, the candidate is
too small, so increase it. When the binary search converges, `low` is the
minimum possible value of the largest subarray sum.

Time Complexity: O(n log(sum(nums)))

Space Complexity: O(1)
"""
class Solution(object):
    def splitArray(self, nums, k):
        low = max(nums)
        high = sum(nums)

        while low < high:
            mid = (low + high) // 2

            parts = 1
            s = 0

            for i in range(len(nums)):
                if s + nums[i] > mid:
                    parts += 1
                    s = nums[i]
                else:
                    s += nums[i]

            if parts <= k:
                high = mid
            else:
                low = mid + 1

        return low