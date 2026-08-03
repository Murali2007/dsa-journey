"""
Problem: Find Minimum in Rotated Sorted Array

Platform: LeetCode

Difficulty: Medium

Approach:

Use Binary Search to locate the minimum element in the rotated sorted array.
Maintain two pointers representing the current search range. At each step,
compute the middle index and compare the middle element with the last element.
If the middle element is greater than the last element, the minimum must lie in
the right half, so move the left pointer to `mid + 1`. Otherwise, the minimum
lies in the left half, including the middle element, so update the right pointer
to `mid`. Continue until both pointers converge. The element at the converged
index is the minimum element in the array.

Time Complexity: O(log n)

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
            else:
                high = mid

        return arr[low]