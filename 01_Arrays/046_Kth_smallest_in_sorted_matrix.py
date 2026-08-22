"""
Problem: Kth Smallest Element in a Sorted Matrix

Platform: LeetCode

Difficulty: Medium

Approach:

Use Binary Search on the range of possible values in the matrix. The minimum
possible value is the top-left element and the maximum possible value is the
bottom-right element. For each candidate value `mid`, count how many elements
in the matrix are less than or equal to `mid`. Since every row and every column
is sorted, start from the top-right corner and use two pointers. If the current
element is less than or equal to `mid`, all elements to its left in that row are
also less than or equal to `mid`, so add `col + 1` to the count and move to the
next row. Otherwise, move the column pointer left. If the count is at least `k`,
the kth smallest value is less than or equal to `mid`, so search the left half.
Otherwise, search the right half. When the search converges, `low` is the kth
smallest element.

Time Complexity: O(n log(max(matrix) - min(matrix)))

Space Complexity: O(1)
"""
class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[-1][-1]

        while low < high:
            mid = (low + high) // 2

            row = 0
            col = n - 1
            h = 0

            while row < n and col >= 0:
                if matrix[row][col] <= mid:
                    h += col + 1
                    row += 1
                else:
                    col -= 1

            if h >= k:
                high = mid
            else:
                low = mid + 1

        return low