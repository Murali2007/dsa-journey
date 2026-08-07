"""
Problem: Find Peak Element

Platform: LeetCode

Difficulty: Medium

Approach:

Use Binary Search to find an element that is greater than its neighboring
elements. First, handle the cases where the array contains only one element or
where either boundary element is a peak. For the remaining elements, perform
Binary Search between the second and second-last positions. If the middle
element is greater than both of its neighbors, it is a peak and its index is
returned. If the left neighbor is greater than the middle element, a peak must
exist in the left half, so move the high pointer to the left. Otherwise, if the
right neighbor is greater, a peak must exist in the right half, so move the low
pointer to the right.

Time Complexity: O(log n)

Space Complexity: O(1)
"""
class Solution(object):
    def findPeakElement(self, arr):
        n = len(arr)

        if n == 1:
            return 0

        if arr[0] > arr[1]:
            return 0

        if arr[n - 1] > arr[n - 2]:
            return n - 1

        low = 1
        high = n - 2

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid

            elif arr[mid] < arr[mid - 1]:
                high = mid - 1

            elif arr[mid] < arr[mid + 1]:
                low = mid + 1