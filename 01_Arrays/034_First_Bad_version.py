"""
Problem: First Bad Version

Platform: LeetCode

Difficulty: Easy

Approach:

Use Binary Search to efficiently identify the first bad version. Maintain a
search range from version 1 to n. At each step, check the middle version using
the provided `isBadVersion()` API. If the middle version is bad, the first bad
version must be at or before it, so continue searching in the left half by
updating the right boundary. Otherwise, the first bad version must lie after the
middle version, so search the right half by updating the left boundary. Continue
until both pointers converge, at which point they indicate the first bad
version.

Time Complexity: O(log n)

Space Complexity: O(1)
"""
class Solution(object):
    def firstBadVersion(self, n):
        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left