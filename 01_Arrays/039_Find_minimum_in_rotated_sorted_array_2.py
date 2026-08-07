"""
Problem: Find Minimum in Rotated Sorted Array II

Platform: LeetCode

Difficulty: Hard

Approach:

Use Binary Search to find the minimum element in a rotated sorted array that
may contain duplicate values. Maintain two pointers representing the current
search range. At each step, compare the middle element with the element at the
right boundary. If the middle element is greater than the rightmost element,
the minimum must be in the right half, so move the left pointer to `mid + 1`.
If the middle element is smaller, the minimum can be at `mid` or in the left
half, so move the right pointer to `mid`. When both elements are equal, it is
not possible to determine which side contains the minimum, so safely reduce the
search range by moving the right pointer one position to the left. Continue
until both pointers converge on the minimum element.

Time Complexity: O(log n) on average, O(n) in the worst case
(due to duplicate elements)

Space Complexity: O(1)
"""
class Solution(object):
    def findMin(self, arr):
        low = 0
        high = len(arr) - 1

        while low < high:
            mid = (low + high) // 2

            if arr[mid] > arr[high]:
                low = mid + 1

            elif arr[mid] < arr[high]:
                high = mid

            else:
                high = high - 1

        return arr[low]