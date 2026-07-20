"""
Problem: Next Permutation

Platform: LeetCode

Difficulty: Medium

Approach:

Traverse the array from right to left to find the first index where the current
element is smaller than the next element. This index represents the pivot where
the next lexicographically larger permutation can be formed. If such a pivot
exists, scan from the end of the array to find the smallest element that is
greater than the pivot and swap them. Finally, reverse the suffix starting just
after the pivot. Reversing the suffix transforms it into the smallest possible
order, producing the next lexicographically greater permutation. If no pivot is
found, the array is in descending order, so reversing the entire array produces
the smallest permutation.

Time Complexity: O(n)

Space Complexity: O(1)
"""
class Solution(object):
    def nextPermutation(self, arr):
        n = len(arr)
        i = n - 2

        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1
            while arr[j] <= arr[i]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]

        left = i + 1
        right = n - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return arr