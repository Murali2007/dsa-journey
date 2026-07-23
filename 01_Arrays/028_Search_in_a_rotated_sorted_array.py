"""
Problem: Search in Rotated Sorted Array

Platform: LeetCode

Difficulty: Medium

Approach:

Use a modified Binary Search to locate the target in the rotated sorted array.
At each step, compute the middle index and determine which half of the array is
sorted. If the left half is sorted, check whether the target lies within that
range. If it does, continue searching in the left half; otherwise, search in the
right half. Similarly, if the right half is sorted, determine whether the target
belongs to that range and adjust the search accordingly. Continue narrowing the
search space until the target is found or the search interval becomes empty.

Time Complexity: O(log n)

Space Complexity: O(1)
"""
class Solution(object):
    def search(self, arr, target):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                return mid

            elif arr[mid] >= arr[low]:
                if arr[low] <= target < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            elif arr[mid] < arr[high]:
                if arr[mid] < target <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1