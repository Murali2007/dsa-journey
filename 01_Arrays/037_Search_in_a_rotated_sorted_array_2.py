"""
Problem: Search in Rotated Sorted Array II

Platform: LeetCode

Difficulty: Medium

Approach:

Use a modified Binary Search to search for the target in a rotated sorted array
that may contain duplicate elements. At each step, compute the middle index. If
the target is found, return True immediately. When the left, middle, and right
elements are equal, it is impossible to determine the sorted half, so shrink the
search range by moving both pointers inward. Otherwise, identify which half of
the array is sorted. If the target lies within the sorted half, continue
searching there; otherwise, search the other half. If the search interval
becomes empty without finding the target, return False.

Time Complexity: O(log n) on average, O(n) in the worst case
(due to duplicate elements)

Space Complexity: O(1)
"""
class Solution(object):
    def search(self, arr, target):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                return True

            if arr[low] == arr[mid] == arr[high]:
                low += 1
                high -= 1

            elif arr[low] <= arr[mid]:
                if arr[low] <= target < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            else:
                if arr[mid] < target <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False