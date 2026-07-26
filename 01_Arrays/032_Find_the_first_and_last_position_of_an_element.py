"""
Problem: Find First and Last Position of Element in Sorted Array

Platform: LeetCode

Difficulty: Medium

Approach:

Use Binary Search twice on the sorted array. The first search locates the first
occurrence of the target by continuing the search toward the left even after
finding the target. The second search locates the last occurrence by continuing
the search toward the right after finding the target. If the target is not found
during the first search, return [-1, -1]. Otherwise, return the indices of the
first and last occurrences.

Time Complexity: O(log n)

Space Complexity: O(1)
"""
class Solution(object):
    def searchRange(self, arr, target):
        l = []

        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                if mid == 0 or arr[mid - 1] != arr[mid]:
                    l.append(mid)
                    break
                else:
                    high = mid - 1

            elif arr[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        if len(l) == 0:
            l.append(-1)

        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                if mid == len(arr) - 1 or arr[mid] != arr[mid + 1]:
                    l.append(mid)
                    break
                else:
                    low = mid + 1

            elif arr[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        if len(l) == 1:
            l.append(-1)

        return l