"""
Problem: Search a 2D Matrix

Platform: LeetCode

Difficulty: Medium

Approach:

Treat the 2D matrix as a single sorted 1D array and apply Binary Search.
Maintain a search range from the first to the last virtual index. At each step,
compute the middle index and convert it back into its corresponding row and
column using division and modulus operations. Compare the value at that position
with the target. If the value is smaller, search the right half; if it is
larger, search the left half. Continue until the target is found or the search
range becomes empty.

Time Complexity: O(log(m × n))

Space Complexity: O(1)
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])

        low = 0
        high = m * n - 1

        while low <= high:
            mid = (low + high) // 2
            value = matrix[mid // n][mid % n]

            if value == target:
                return True

            elif target > value:
                low = mid + 1

            else:
                high = mid - 1

        return False