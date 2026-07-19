"""
Problem: Search Insert Position

Platform: LeetCode

Difficulty: Easy

Approach:

Use Binary Search to efficiently locate the target element in the sorted array.
Maintain two pointers representing the current search range. At each step,
calculate the middle index and compare its value with the target. If the target
is found, return its index immediately. If the middle element is smaller than
the target, continue searching in the right half; otherwise, search in the left
half. If the target is not present after the search completes, the low pointer
will indicate the correct position where the target should be inserted while
maintaining the sorted order.

Time Complexity: O(log n)

Space Complexity: O(1)
"""
class Solution(object):
    def searchInsert(self, arr, target):
        n = len(arr)
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return low